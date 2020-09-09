#!/usr/bin/perl -w
#/***************************************************************************************
# *
# * Copyright (c) 2008,2009 Nuno Fonseca. All rights reserved.
# * This code is freely available for academic purposes.
# * If you intend to use it for commercial purposes then please contact the author first.
#
# * Author: Nuno A. Fonseca 
# * Date: 2008-03-15
# * $Id$
# *
# ******************************************************************************************/

=head1 NAME

sigdis.pl - signature discovery in genomic and proteomic sequences

=head1 SYNOPSIS

Usage:
    sigids.pl  -p posfile -n negfile -l max_pat_len -minpos float -maxneg float [-e --sim float] ...  [-v verbose] [-h --help]

=head1 DESCRIPTION

The options are:
    -p --posfile filename - file containing sequences in fasta format. [required]
    -n --negfile filename - file containing sequences in fasta format. [required]
    --minpos float        - minimum percentage of sequences in posfile where an acceptable pattern must be observed. [required]
    --maxneg float        - maximum percentage of sequences in negfile where an acceptable pattern must be observed. [required]

    -e --sim float       - similarity between the seed and the pattern
                            [default: 0.50]

    -t --train float     - percentage of sequences used for training/discovering the patterns.
                            [default: 0.50]
    -l --maxexpand       - maximum number of positions expanded.
                            [default: 10]

    -w --seedlen         - minimum seed length.
                            [default: 3]

    -i --input           - input sequences type (dna,prot).
                            [default: prot]
    -r --refine pattern  - refine the given pattern.
    -s --score  pattern  - compute the score of the given pattern.
    -v --verbose         - toogle to a more verbose execution of the program.
    -h --help            - this help menu.

=head1 AUTHOR

Nuno A. Fonseca, nunofonseca-at-acm-org

=cut
use strict;

use Number::Format qw (round);
use Getopt::Long;

use Bio::SeqIO;
use List::Util 'shuffle';

# default values
my $res_file    = "";
my $pat2test    = "";
my $gen_split   = 1;# reuse the existing train/test files?
my $seed        = "";
my $minwordlen  = 3;
my $train_per   = 0.5;
my $e_sim       = 0.5;#estimated similiarity among the sequences
#my $gui         = $opt_g ? $opt_g: "no";

my $posfile="";
my $negfile="";
my $minpos="";
my $maxneg="";
my $minpos_user="";
my $maxneg_user="";
my $max_pat_expand=10;#L
my $verbosity = 2; # values: 0,1,2,3,4,5
my $printed_label=0;
my $minpos_w;
my $maxneg_w;
my $words_file;
my $input_data_type="prot";
my $pdx_itype="-p";
######################################################
my $expand_max_alt_prot=6;# maximum number of residues allowed at each position when expanding
my $expand_max_alt_dna=2;# maximum number of residues allowed at each position when expanding
my $expand_max_alt;
# 
my $wd_cmd="wd";
my $wd_args="-x -2 -v 0";
my $pdx_cmd="pdx";
my $maximal_words_cmd="maximal_words";
my $max_it_gen=40;# maximum number of generalizations performed on a word (generalize procedure)

###################################################################################################
# Private
my $version="0.3.1";

my $prefix;
my $test_posfile;
my $test_negfile;
my $train_posfile;
my $train_negfile;

my $npos;
my $nneg;
my $train_npos;
my $train_nneg;
my $test_npos;
my $test_nneg;

my $best_word_stats="";
my $best_pat_stats="";
my $best_word="";
my $best_pat="";
###################################################################################################
# 
GetOptions(
    'e|sim:f'         => \$e_sim,
    't|train=f'       => \$train_per,
    'l|maxexpand:i'   => \$max_pat_expand,
    'w|seedlen:i'     => \$minwordlen,
    'p|posfile=s'     => \$posfile,
    'n|negfile=s'     => \$negfile,
    'minpos:f'        => \$minpos,
    'maxneg:f'        => \$maxneg,
    'i|input:s'       => \$input_data_type,
    'r|refine:s'      => \$seed,
    's|score:s'       => \$pat2test,

    'v|verbosity:i'     => \$verbosity,
    'h|?|help'        => sub{ help(); },
    );

###################################################################################################
#
sub header {
    print "SigDis v$version.\n";
}

sub help {
    exec('perldoc',$0);
    exit(0);
}

sub check_cmdline_args {
    my $numArgs = scalar(@ARGV);

#    if ( $numArgs < 4 ) {
#	help();
#    }
    $minpos_user=$minpos;
    $maxneg_user=$maxneg;
    # check if the files exist and are readable
    if (! (-e "$posfile") || ! (-r "$posfile") ) { 
	print STDERR "Error: unable to access $posfile.\n";
	exit(1);
    }
    if (! (-e "$negfile") || ! (-r "$negfile" ) ) { 
	print STDERR "Error: unable to access $negfile.\n";
	exit(1);
    }
    if ( $minpos eq "" || $maxneg eq "" ) {
	help();
    }
    # check the numbers
    if (! ($minpos =~ qr{^[01]\.\d+$} ) ) {
	print STDERR "Error: invalid value minpos: $minpos\n";
	exit(1);
    }
    if (! ($maxneg =~ qr{^0|1\.\d+$} )) {
	print STDERR "Error: invalid value maxneg: $maxneg\n";
	exit(1);
    }
    if (! ($train_per =~ qr{^0.\d+$} )) {
	print STDERR "Error: invalid value -t: $train_per\n";
	exit(1);
    }
    if (! ($e_sim =~ qr{^0.\d+$} )) {
	print STDERR "Error: invalid value -e: $train_per\n";
	exit(1);
    }
    if (! ($verbosity =~ qr{^\d+$} ) || $verbosity<0 || $verbosity>10) {
	print STDERR "Error: invalid value verbosity: $verbosity\n";
	exit(1);
    }
    ###############
    # ... complete!
    
    #
    if ( $input_data_type eq "prot" ) {
	$expand_max_alt=$expand_max_alt_prot;
	$pdx_itype="-p";
    } else {
	$expand_max_alt=$expand_max_alt_dna;
	$pdx_itype="-d";
    }
}
#
#
#
sub set_best_pat ($$) {
    my $spat=$_[0];
    my $pat=$_[1];
    if ($best_pat_stats eq "") {
	$best_pat_stats=$spat;
	$best_pat=$pat;
	return;
    }
    $spat=~/(\d+) (\d+)/;
    my $pos=$1;    my $neg=$2;
    $best_pat_stats=~/(\d+) (\d+)/;
    my $bpos=$1;   my $bneg=$2;
    if ( ($bpos-$bneg)<($pos-$neg) ) {
	$best_pat_stats=$spat;
	$best_pat=$pat;
    }
}

sub fasta2flat {
    my ($ifile)=@_;

    my $ctr=0;
    my $in = new Bio::SeqIO(-format => "fasta", -file   => $ifile) or die "Unable to open $ifile";
    open(FD,">$$.$ifile") or die ("Unable to create temporary file $$.$ifile");
    while( my $seq = $in->next_seq ) {
	print FD ">".$seq->id()."\n" ;
	print FD $seq->seq."\n" ;
	++$ctr;
    }    
    close(FD);
    `mv $$.$ifile $ifile`;
    return $ctr;
}

sub initial_stats {

    # compute the average length size (pos, neg, and both) and stddesv
}

# splits the src fasta file into 2 files (filename1 and filename2) by randomly placing $file1_nels
# sequences into file1 and the remaining sequences in file2.
# two extra files (extension .seq) that contain the sequences without the fasta headers.
sub split_fasta_randomly {

    my ($src,$file1,$file2,$file1_nels)=@_;
    
    my @ids=split(/\n/,`grep "^>" $src`);
    my @shuffled = shuffle(@ids);
    my %file1_ids;
    my %file2_ids;    

    for my $el (@shuffled) {
	if ( $file1_nels > 0 ) {
	    $file1_ids{$el}=1;
	} else {
	    $file2_ids{$el}=1;
	}
	$file1_nels--;
    }

    open(FD1,">$file1") || die ("Unable to create file $file1.");
    open(FD11,">$file1.seq") || die ("Unable to create file $file1.seq");

    open(FD2,">$file2") || die ("Unable to create file $file2.");
    open(FD21,">$file2.seq") || die ("Unable to create file $file2.seq");
    
    my $in = new Bio::SeqIO(-format => "fasta", -file   => $src);

    while( my $seq = $in->next_seq ) {
	my $id=$seq->id();
	if ( $file2_ids{">$id"} ) {
	    print FD2 ">$id\n";
	    print FD2 $seq->seq()."\n";
	    print FD21 $seq->seq()."\n";
	} else {
	    print FD1 ">$id\n";
	    print FD1 $seq->seq()."\n";
	    print FD11 $seq->seq()."\n";
	}
    }    
    close(FD1);
    close(FD2);
    close(FD11);
    close(FD21);
}



sub initialize  {
    
    if ($res_file ne "") {
	$prefix=$res_file;
	# create a link to the original data files with the defined prefix
	`rm -f ${prefix}_$posfile ${prefix}_$negfile`;
	`ln -s $posfile ${prefix}_$posfile`;
	`ln -s $negfile ${prefix}_$negfile`;
	$posfile="${prefix}_$posfile";
	$negfile="${prefix}_$negfile";
    } else {
	$prefix="";
    }
    $train_posfile="$posfile.train.seq";
    $train_negfile="$negfile.train.seq";
    $test_posfile="$posfile.test";
    $test_negfile="$negfile.test";
    
    if ( $seed eq "" && $pat2test eq "" ) { 
	################################
	# convert the fasta file to .seq
	# number of examples
	# flatten fasta file
	$npos=fasta2flat($posfile);
	$nneg=fasta2flat($negfile);
	$train_npos=round(($npos*$train_per),0);
	$train_nneg=round(($nneg*$train_per),0);
	$test_npos=$npos-$train_npos;
	$test_nneg=$nneg-$train_nneg;
	
	pmsg("Sequences(+,-)=($npos,$nneg)\n",1);
	if ( $gen_split==1 ) {
	    pmsg("Generating train/test files\n",1);
	    split_fasta_randomly($posfile,$train_posfile,$test_posfile,$train_npos);
	    split_fasta_randomly($negfile,$train_negfile,$test_negfile,$train_nneg);
	} else {
	    # just check if the files exist
	    if (! (-e "$train_posfile") || ! (-r "$train_posfile")) {
		perror("Unable to read/find $train_posfile.");
		exit(1);
	    }
	    if ( ! (-e "$train_negfile") || ! (-r "$train_negfile") ) {
		perror("Unable to read/find $train_negfile.");
		exit(1);
	    }
	    if (! (-e "$test_posfile") || ! (-r "$test_posfile")) {
		perror("Unable to read/find $test_posfile.");
		exit(1);
	    }
	    if (! (-e "$test_negfile") || ! (-r "$test_negfile") ) {
		perror("Unable to read/find $test_negfile.");
		exit(1);
	    }
	    pmsg("Found train/test files\n",1);
	}
#	
	pmsg("...$train_posfile: $train_npos\n",1);
	pmsg("...$train_negfile: $train_nneg\n",1);
	pmsg("...$test_posfile: $test_npos\n",1);
	pmsg("...$test_negfile: $test_nneg\n",1);
    } else {
	$npos=`grep ">" $posfile | wc -l | cut -f 1 -d\\ `; chomp $npos;
	$nneg=`grep ">" $negfile | wc -l | cut -f 1 -d\\ `; chomp $nneg;
	$train_npos=round(($npos*$train_per),0);
	$train_nneg=round(($nneg*$train_per),0);
	$test_npos=$npos-$train_npos;
	$test_nneg=$nneg-$train_nneg;
    }
    $minpos=$train_npos*$minpos;
    $maxneg=$train_nneg*$maxneg;

    #pmsg("$train_posfile: $train_npos $train_nneg",2);
    $minpos_w=$minpos*$e_sim; 
    $maxneg_w=($maxneg>0?$maxneg*(1+$e_sim/2):1);
#    $maxneg_w=$maxneg;
    return;
}
#
# Computes the number of matches a motif in the given file
#
sub num_matches ($$) {
    my $n=`grep -v "^>" $_[1] | grep -c "$_[0]"` or die $?;
    $n =~ s/^\s+|\s+$//g; # trim
#    print "<>$_[0] -- $_[1] -- $n<>\n";
    return $n;
}
# recall: matches(p,S1)/|S1|
# precision: matches(p,S1)/(matches(p,S1)+matches(p,S2))
# f=2*precision*recall/(recall+precision)
sub _stats {
    my $pat=$_[0];
    my $pos_file=$_[1];
    my $neg_file=$_[2];
    my $npos=$_[3];
    my $nneg=$_[4];

    my $POS=num_matches($pat,$pos_file);
    my $NEG=num_matches($pat,$neg_file);
#    print ">>$pat $pos_file $POS $neg_file $NEG\n";
    my $recall=round(($POS/$npos),3);
    my $recall_neg=round(($NEG/$nneg),3);
    my $prec;
    my $f;
    if ( ($NEG+$POS)==0 ) {
	$prec=0.0;
    } else {
	$prec=round($POS/($NEG+$POS),3);
    }
    if ( ($prec+$recall)==0 ) {
	$f=0.0;
    } else {
	$f=round(2*$prec*$recall/($prec+$recall),3);
    }
    if ( $printed_label==0 ) {
	print "+ - recall recall_neg prec f tpos tneg\n";
	$printed_label=1;
    }
    if ($recall>1) {
	print "RECALL>1?! $POS $NEG $recall $recall_neg $prec $f $npos $nneg\nnum_matches($pat,$pos_file)";
    }
#    print ">>>>>>>>>>>>>.".($recall*(1-$recall)/$npos)."<<<<<<<<<<";
    my $std_desv_pos=round(sqrt($recall*(1-$recall)/$npos),4);
    my $std_desv_neg=round(sqrt($recall_neg*(1-$recall_neg)/$nneg),4);
    return "$POS $NEG $recall $recall_neg $prec $f $std_desv_pos $std_desv_neg";
}
#
#
#
sub pat_stats {
    my $pat=$_[0];
    return _stats($_[0],$train_posfile,$train_negfile,$train_npos,$train_nneg);
}
#
#
#
sub pat_testset_stats {
    return _stats($_[0],$test_posfile,$test_negfile,$test_npos,$test_nneg);
}
#
# return the f measure
#
sub pat_stats_f ($) {
    my $s=$_[0];
    $s=~ /([0-9\.]+) ([0-9\.]+) ([0-9\.]+) ([0-9\.]+) ([0-9\.]+) ([0-9\.]+)/;
    return $6;
}
sub pat_stats_neg ($) {
    my $s=$_[0];
    $s=~ /([0-9\.]+) ([0-9\.]+) ([0-9\.]+) ([0-9\.]+) ([0-9\.]+) ([0-9\.]+)/;
    return $2;
}
#
#
#
sub pinfo ($) {
    print "Info: $_[0]";
}
sub pmsg ($$) {
    my $msg=$_[0];
    my $level=$_[1];
    if ($level<=$verbosity) {
	print STDERR "$_[0]";
    }
}
#
#
#
sub perror {
    print STDERR "ERROR: $_[0]";
}
#
# $1 - file
# $2 - word column
sub maximal_words {
    `$maximal_words_cmd $_[0] "-" $_[1]`;
    my $fd1;
    my $fdw;
    open fd1, "$_[0].max" or die $!;
    open fd2, ">$_[0].tmp" or die $!;
    while (<fd1>) {
	if (/(\S+) /) { 
	    print fd2 `grep -F "$1" $_[0]`;
	}
    }
    close fd1;
    close fd2;
    `mv $_[0].tmp $_[0]`;
}
#
#
#
sub generalize {
    
    my $word=$_[0];
    my $pdx_extra=$_[1];
    my $pat1;
    my $patt=$word;
    my $bstats=pat_stats($patt); my $v=pat_stats_f($bstats);
    my $i;
    my $stats="";
    my $v2=0;
    my $negs=pat_stats_neg($bstats);
    if ($negs>=$maxneg_w) { $negs=$maxneg_w; 
    } else{ 
	if ($negs>$maxneg) { $negs=$maxneg; } # the increase in coverage can not be made at the expense of increasing the number of examples too much
    }
    pmsg(">Generalizing $patt $bstats/$negs\n",1);
    for($i=1;$i<=$max_it_gen;++$i) {	
#	print "$pdx_cmd $pdx_extra -x -t 2 --seed=\"$patt\" -q $train_posfile -n $train_negfile -p 2 -m $minpos -c $negs\n";
	$pat1=`$pdx_cmd $pdx_extra -x -t 2 --seed="$patt" -q $train_posfile -n $train_negfile $pdx_itype 2 -m $minpos -c $negs 2> /dev/null | grep "pattern =" | cut -f 2 -d=`; 
	pmsg("-$i->$patt->$pat1\n",5);
	$pat1 =~ s/^\s+|\s+$//g;
	$pat1 =~ s/.*\[\].*/-/;
        if ( $pat1 ne "-" ) {       
	    $stats=pat_stats($pat1); 
	    $v2=pat_stats_f($stats);
	}
	if ( "$pat1" eq "$patt" || $v2<$v  ) { # the f-value must remain the same or increase
	    pmsg("-$i->X\n",3);
	    $stats=pat_stats($patt);
	    pmsg("<Generalizing $patt $stats\n",1);
	    return $patt;
	}
	$v=$v2;
	pmsg("-$i->$pat1 - $stats\n",3);
	$patt=$pat1;
    }
    if ($i>$max_it_gen) {
	pmsg("->!\n",3);
    }
    $stats=pat_stats($patt);
    # try to generalize further by looking at residues properties at each position?
    pmsg("<Generalizing $patt $stats\n",1);
    return $patt;
}
#
#
#
sub words_stats_filter  {
    # words file
    my $FILE=$_[0];
    my $fd;

    open fd1,$FILE or die $!;
    open fd2,">$FILE.tmp" or die $!;
    while (<fd1>) {
	my $pos;
	my $w;
# output when using statistical filter	exit(0);
#	/([0-9]+)\/[\ 0-9]*. ([a-zA-Z]+)/; $pos=$1; $w=$2;
# without statistical filter (num_matches num_lines_matched len word)
	/(\d+) (\d+) (\d+) (\S+)/; $pos=$2;$w=$4;
	if ( $pos >= $minpos_w ) {
	    my $negs_matched=`grep -F -c "$w" $train_negfile`;
#	    $negs_matched =~ s/^\s+|\s+\n?$//g; # trim
	    chomp $negs_matched;
#	    print "$pos $negs_matched=\n";
	    my $diff=$pos-$negs_matched;
	    if ( $negs_matched<=$maxneg_w ) {
		print fd2 "$pos $negs_matched $diff $w\n";
	    }
	}
    }
    close fd1;
    close fd2;
    `mv $FILE.tmp $FILE`;
}
#
#
#
sub gen_seeds {
    my $WORDS_FILE=$_[0];
    my $wd_redirect_err;
    if ( $verbosity>3 ) {
	$wd_redirect_err="";
    } else {
	$wd_redirect_err=" 2> /dev/null";
    }
    pmsg(">Generating seeds...\n",1);
    # remove previous conf file
    `rm -f $posfile.wd.conf`;
    pmsg(">Searching for seeds (wd)...\n",2);
    # ------------------------------------
    # run wd
    # setup configuration file
    print "$wd_cmd $wd_args -e $minpos_w -m $minwordlen -c $train_posfile -f $posfile.wd.conf $wd_redirect_err\n";
    `$wd_cmd $wd_args -e $minpos_w -m $minwordlen -c $train_posfile -f $posfile.wd.conf $wd_redirect_err`;
#    `$wd_cmd $wd_args -e $minpos_w -m $minwordlen -c $train_posfile -f $posfile.wd.conf 2>/dev/null`;
    # run it 
    print "$wd_cmd -f $posfile.wd.conf $wd_redirect_err\n";
    `$wd_cmd -f $posfile.wd.conf $wd_redirect_err`;
    # output words to file -s?
    print "$wd_cmd -f $posfile.wd.conf  -e $minpos_w -n -p  > $WORDS_FILE $wd_redirect_err\n";
    `$wd_cmd -f $posfile.wd.conf  -e $minpos_w -n -p  > $WORDS_FILE $wd_redirect_err`;
    # number of words
    my $nwords=`wc -l $WORDS_FILE | cut -f1 -d\\ `;
    pmsg("$WORDS_FILE: wd >> $nwords\n",2);
    if ( $nwords>0 ) {
	# filter words using positive and negative matches 
        $nwords=words_stats_filter $WORDS_FILE;
	$nwords=`wc -l $WORDS_FILE | cut -f1 -d\\ `;
	pmsg("$WORDS_FILE: stats filter >> $nwords\n",2);
	# maximal words 
        maximal_words($WORDS_FILE,4);
	$nwords=`wc -l $WORDS_FILE | cut -f1 -d\\ `;
	chomp $nwords;
	pmsg("$WORDS_FILE: maximal filter >> $nwords\n",2);
    } 
    pmsg("<Generating seeds: $nwords seeds\n",1);
    return $nwords;
}
#
#
#
sub refine {

    my $pat=$_[0];
    my $pdx_extra=$_[1];
    my $i;
    pmsg("Refine $pat\n",2);
#    print "$pdx_cmd $pdx_extra -x -r -t 2 --seed=\"$pat\" -q $train_posfile -n $train_negfile -p 2 -m $minpos -c $maxneg  | grep \"pattern =\" | cut -f 2 -d=`";
    my $pat1=`$pdx_cmd $pdx_extra  -r -t 20 --seed="$pat" -q $train_posfile -n $train_negfile  $pdx_itype  2 -m $minpos -c $maxneg 2>/dev/null | grep "pattern =" | cut -f 2 -d=`; 
#    my $pat1=`$pdx_cmd $pdx_extra -x -r -t 2 --seed="$pat" -q $train_posfile -n $train_negfile -p 2 -m $minpos -c $maxneg  | grep "pattern =" | cut -f 2 -d=`; 
    #}
    $pat1 =~ s/^\s+|\s+$//g; # trim
    $pat1 =~ s/(\[\])/\./g; # replace [] by .
    pmsg("Refine $pat---> $pat1\n",2);
    return $pat1;
}
#
#
#
sub lets2pat {    
    my $l=length($_[0]);
    if ( $l == 1 ) { return $_[0]; }
    if ( $l > $expand_max_alt  ) { return "."; }
    return "[$_[0]]";
}
#
#
#
sub refine_expand {
    my $best=$_[0];
    my $i;
    
    # stats
    my $best_stats=pat_stats($best); $best_stats=~/(\d+) (\d+)/;
    my $best_neg=$2;
    my $best_pos=$1;
    my $best_val=pat_stats_f($best_stats);
    my $neg;
    my $pos;
    my $npat=$best;
    #
    #print "$best_stats>$best_neg<>$maxneg<\n";
    pmsg(">refine_expand $best $best_stats\n",2);
    if ( $best_pos < $minpos || $best_neg == 0) { 
	pmsg("<refine_expand $best $best_stats\n",2);
	return $best; 
    } ;# unable to improve
    #print STDERR ">>>$best\n";
    for ( $i=1;$i<$max_pat_expand;$i++) {
	my $r1;
	my $r2;
	my $npat1=$npat;
	my $w=`grep -o ".$npat." $train_posfile > $$.tmp`;    
	my $pos1=`cut -b 1 $$.tmp | sort -u | tr "\n" " "| sed "s/ //g"`;
	my $l=`wc -L $$.tmp |sed "s/ .*//"`;
	$l =~ s/^\s+|\s+$//g; # trim
	my $pos2=`cut -b $l  $$.tmp | sort -u | tr "\n" " "| sed "s/ //g"`;
	$r1=lets2pat($pos1);
	$r2=lets2pat($pos2);
	$npat1="$r1$npat1$r2";	
	pmsg("$npat1\n",4);
	$npat1=refine($npat1," -e 1 ");
	$npat1=refine($npat1," -e 1 ");
	$npat1=refine($npat1," -e 2 ");
	$npat1=refine($npat1," -e 2 ");
	$npat1=refine($npat1," -e 3 ");
	my $s=pat_stats($npat1);
	pmsg("END($i):-$npat1-$s\n",2);
	#my $pat1=generalize($npat1," -e 3 ");
	# Stop expand/refining when there is no gain in doing it
	my $stats=pat_stats($npat1); $stats=~/(\d+) (\d+)/; $pos=$1; $neg=$2;
	set_best_pat($stats,$npat1);
#	if ( $neg <= $maxneg ) { 
#	    pmsg("<refine_expand $npat1 $stats\n",2);
#	    return $npat1; 
#	}
	if ( $pos <= $minpos ) { 
	    pmsg("<refine_expand $best $best_stats\n",2);
	    return $best; 
	}
	if ( ($best_pos-$best_neg)==($pos-$neg) || ($best_val>pat_stats_f($stats)) ) {
	    # no improvement
	    $npat=$npat1;
	} else { 
	    $best_stats=$stats;
	    $best=$npat1; 
	    $npat=$best;
	    $best_val=pat_stats_f($stats);
	}
    }
    pmsg("<refine_expand $best $best_stats\n",2);
    return $best;
}
#
#
#
sub word2pattern {
    my $seed=$_[0];
    
    pmsg(">word2pattern $seed\n",2);
    my $pat1=generalize($seed,"");
    $pat1=refine_expand($pat1);    $pat1 =~ s/^\.+|\.+$//; # trim
    pmsg("<word2pattern $seed->$pat1\n",2);
    return $pat1;
}
#
#
#
sub generalize_words {
    my $WORDS_FILE=$_[0];
    my $PAT_FILE=$_[1];
    my $nseeds=$_[2];
    my $word;
    my $fd1;
    my $npats=0;
    my $i;

    open fd1, $WORDS_FILE;
    open fd2, ">$PAT_FILE";
    pmsg(">Generalize seeds ($nseeds)...\n",2);
    while ( <fd1> ) {
	/(\d+).(\d+).(-*\d+).(\S+)/;#.-> be tolerant with how the fields are separated
	$seed=$4;
	my $pat=word2pattern($seed);
	#$pat;
	if ( "$pat" eq "" ) {
	    $pat=$seed;
	}
	my $stats=pat_stats($pat);$stats=~/(\d+) (\d+)/;my $pos=$1; my $neg=$2;
	set_best_pat($stats,$pat);
	if ( $pos >=$minpos && $neg <=$maxneg ) {
	    my $matches=`grep -F -c " $pat " $PAT_FILE`;
	    chomp $matches;
	    if ( $matches>0 ) {
		pmsg("$stats $pat $seed Redundant\n",2);
	    } else {
		my $test_stats=pat_testset_stats($pat);
		pmsg("FOUND: $stats $test_stats $pat $seed\n",1);
		print fd2 "$stats $test_stats $pat $seed\n";
		$npats++;
	    }
	} else {
	    pmsg("Discarded: $stats $pat $seed ($minpos/$maxneg)\n",2);
	}		    
	$i++;
    }
    close fd2;
    pmsg("<Generalize seeds ($nseeds)->$npats motifs\n",2);
    return $npats;    
}
sub sort_pats {
    my $file=$_[0];    
    `sort -k 9,13 -g -r $file > $$; mv $$ $file;`
}

sub cover_set {
    my $pat_file=$_[0];
    my $seqs_file=$_[1];
    my $nseqs_covered=0;
    my $cover_file="$seqs_file.cover";
    open fd2, ">$cover_file";
    `cp $seqs_file $seqs_file.tmp`;
    $seqs_file="$seqs_file.tmp";
    open fd1, $pat_file;
    while ( <fd1> ) {	
	my $line=$_;
	$line =~ s/^\s+|\s+$//g; # trim
	my $pat;
#	if (/^(\d+) (\d+) (\S+) (\S+) (\d+) (\d+) (\S+) (\S+) (\S+) (\S+) ([A-Za-z\]\[\^]+) (\S+)$/ )

	if ( $line=~/ ([^ ]+) ([A-Za-z]+)$/ ) {
	    $pat=$1;
	} else {
	    print("error reading $pat-file: $_");
	    exit(1);
	}
	#print ">>$_>>>$pat\n";
	my $matches=`grep -B 1 "$pat" $seqs_file | grep ">" | tr "\n" ";"`; chomp $matches;
	if ( $matches ne "" ) {
#	    print ">>>>>>>>>>$matches<<<>>>$pat<<<<>>>>$$>>>>$line\n";
	    `grep -B 1 -v "$pat" $seqs_file > $$.tmp; mv $$.tmp $seqs_file`;
	    print fd2 "$line ;$matches\n";
	}
    }   
    close fd1;
    close fd2;
# number of sequences matched
    $nseqs_covered=`cat $cover_file| tr ";" "\n" | grep ">" | sort -u | wc -l`;
#    print("Covered($cover_file):$nseqs_covered\n");
    return $nseqs_covered;
}


#
#
#
my $stats;
check_cmdline_args;

header();
initialize;

if ($seed ne "") {
    my $pat=word2pattern($seed);
    $stats=pat_stats($pat);
    print "$stats $pat\n";
    exit(0);
}
# evaluate the pattern
if ($pat2test ne "") {
    $stats=pat_stats($pat2test);
    print "$stats $pat2test\n";
    exit(0);
}

$words_file="$posfile.words";
my $pat_file="$posfile.pat";
my $nseeds=gen_seeds($words_file);
#my $nseeds=1;
if ( $nseeds==0 ) {
    pinfo "Unable to find seeds with the given settings\n";
    my $newval1=($minpos_user-0.1>0?$minpos_user-0.1:0.01);
    pinfo "You may try: $newval1 (instead of $minpos_user) or/and...\n";
    my $newval2=($maxneg_user+0.05<0.2?$maxneg_user+0.05:0.2);
    pinfo "you may try: $newval2 (instead of $maxneg_user) or/and...\n";
    $newval2=($e_sim-0.05>0?$e_sim-0.05:0.05);
    pinfo "you may try to decrease the expected similiarity: -e $newval2\n";
    exit(0);
}
my $numpats=generalize_words($words_file,$pat_file,$nseeds);
pinfo "generalize_words($words_file,$pat_file,$nseeds) complete\n";

if ($numpats==0) {
    pinfo "Unable to find a pattern with the given settings.\n";
    pinfo "Best pattern stats found: $best_pat_stats - $best_pat\n";
    my $newval1=($minpos_user-0.1>0?$minpos_user-0.1:0.01);
    pinfo "You may try: $newval1 (instead of $minpos_user) or/and...\n";
    my $newval2=($maxneg_user+0.05<0.2?$maxneg_user+0.05:0.2);
    pinfo "you may try: $newval2 (instead of $maxneg_user) or/and...\n";
    exit(0);
}
# sort the patterns according to the score obtained
pinfo "sorting patterns $pat_file\n";
sort_pats($pat_file);
pinfo "patterns in $pat_file sorted\n";

# Motif
my $postcover=round(cover_set($pat_file,"$posfile.train.seq")/$train_npos,3);
my $negtcover=round(cover_set($pat_file,"$negfile.train.seq")/$train_nneg,3);
my $posucover=round(cover_set($pat_file,"$posfile.test.seq")/$test_npos,3);
my $negucover=round(cover_set($pat_file,"$negfile.test.seq")/$test_nneg,3);
pmsg("Coverage: train+=$postcover train-=$negtcover test+=$posucover test-=$negucover\n",2);
