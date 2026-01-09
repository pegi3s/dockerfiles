#!/bin/bash

echo "Running....."

docker_dir=$1
dir=/data
rh_dir=/ipssa_project/pipeline_working_dir/input/3_renamed_headers
ma_dir=/ipssa_project/pipeline_working_dir/input/8_master_alignment
mar_dir=/ipssa_project/pipeline_working_dir/input/9_master_alignment_renamed
codeml_dir=/ipssa_project/pipeline_working_dir/pss_subsets
codeml_oa_dir=/original_alignment/codeml/fasta_checked
codeml_results=/original_alignment/codeml/results/
tcoffee_dir=/ipssa_project/pipeline_working_dir/input/6_aligned
phipack_dir=/ipssa_project/pipeline_working_dir/pss_subsets

alimethod=$(grep "align_method=" $dir/ipssa-project.params  | cut -f2 -d'=') 
cd $dir/$ma_dir && ls > /tmp/tmp1

START=1
END=$(grep "codeml_runs=" $dir/ipssa-project.params  | cut -f2 -d'=')
for i in $(eval echo "{$START..$END}")
do

while read gene
do


mkdir -p $dir/codeml_projects/$gene.$i/$alimethod/

chmod -R 777 $dir/codeml_projects/



#FILES IN $gene

#input.fasta
cp $dir/$codeml_dir/$gene/original_alignment/codeml/fasta_checked/$gene.$i $dir/codeml_projects/$gene.$i/input.fasta
sed -i 's/-//g' $dir/codeml_projects/$gene.$i/input.fasta


#names.txt
cp $dir/$rh_dir/$gene.headers_map $dir/codeml_projects/$gene.$i/names_tmp.txt


awk '{ print $2 "\t" $1}' $dir/codeml_projects/$gene.$i/names_tmp.txt | sed 's/>//g; s/\t/ - /g' > $dir/codeml_projects/$gene.$i/names.txt

rm $dir/codeml_projects/$gene.$i/names_tmp.txt


#empty project.conf
touch $dir/codeml_projects/$gene.$i/project.conf



mkdir -p $dir/codeml_projects/$gene.$i/$alimethod/allfiles/
mkdir -p $dir/codeml_projects/$gene.$i/$alimethod/allfiles/codeml
mkdir -p $dir/codeml_projects/$gene.$i/$alimethod/allfiles/mrbayes
mkdir -p $dir/codeml_projects/$gene.$i/$alimethod/allfiles/tcoffee



#FILES IN $gene/$alimethod/allfiles

#GETTING CODEML FILES

#codeml.ctl
cp $dir/$codeml_dir/$gene/$codeml_results/$gene.$i/codeml.ctl $dir/codeml_projects/$gene.$i/$alimethod/allfiles/codeml/

#input.fasta.fasta.out
cp $dir/$codeml_dir/$gene/$codeml_results/$gene.$i/$gene.$i.codeml.out $dir/codeml_projects/$gene.$i/$alimethod/allfiles/codeml/input.fasta.fasta.out

#input.fasta.fasta.tree
cp $dir/$codeml_dir/$gene/gapped_alignment/codeml/mrbayes/$gene.$i/mrbayes_tree_without_branch_lengths.tre $dir/codeml_projects/$gene.$i/$alimethod/allfiles/codeml/input.fasta.fasta.tree.tmp
count=$(cat $dir/codeml_projects/$gene.$i/$alimethod/allfiles/codeml/input.fasta.fasta.tree.tmp | sed 's/\,/\n/g' | wc -l)
echo $count" 1" > $dir/codeml_projects/$gene.$i/$alimethod/allfiles/codeml/count.tmp1
echo "" >> $dir/codeml_projects/$gene.$i/$alimethod/allfiles/codeml/count.tmp1
cat $dir/codeml_projects/$gene.$i/$alimethod/allfiles/codeml/count.tmp1 $dir/codeml_projects/$gene.$i/$alimethod/allfiles/codeml/input.fasta.fasta.tree.tmp > $dir/codeml_projects/$gene.$i/$alimethod/allfiles/codeml/input.fasta.fasta.tree
rm $dir/codeml_projects/$gene.$i/$alimethod/allfiles/codeml/input.fasta.fasta.tree.tmp $dir/codeml_projects/$gene.$i/$alimethod/allfiles/codeml/count.tmp1

#GETTING MR. BAYES FILES

#input.fasta.fasta.mrb.con
cp $dir/$codeml_dir/$gene/gapped_alignment/codeml/mrbayes/$gene.$i/mrbayes_input.nex.con.tre $dir/codeml_projects/$gene.$i/$alimethod/allfiles/mrbayes/input.fasta.fasta.mrb.con



#GETTING T-COFFEE FILES

gene_mod=$(echo $gene | sed 's/\.result//g')

#input.fasta.fasta
cp   $dir/$codeml_dir/$gene/$codeml_oa_dir/$gene.$i  $dir/codeml_projects/$gene.$i/$alimethod/allfiles/tcoffee/input.fasta.fasta

#input.fasta.fasta.prot.fasta
cp $dir/$tcoffee_dir/$gene_mod.fasta_aln $dir/codeml_projects/$gene.$i/$alimethod/allfiles/tcoffee/input.fasta.fasta.prot.fasta

#input.prot.fasta.$alimethod.fasta.html
cp $dir/$tcoffee_dir/$gene_mod.html $dir/codeml_projects/$gene.$i/$alimethod/allfiles/tcoffee/input.prot.fasta.$alimethod.fasta.html

#GETTING 'mrbayes.log' AND 'mrbayes.log.psrf' FILES

cd $dir/ipssa_project/pipeline_working_dir/logs && ls run-mrbayes_*[13579].out.log > /tmp/tmp2
	
while read name
do

if grep -q $gene $name; then
cp $name $dir/codeml_projects/$gene.$i/$alimethod/allfiles/mrbayes/mrbayes.log
awk '/Estimated marginal/,/runs converge/' $dir/codeml_projects/$gene.$i/$alimethod/allfiles/mrbayes/mrbayes.log > $dir/codeml_projects/$gene.$i/$alimethod/allfiles/mrbayes/mrbayes.log.psrf
		
fi

done < /tmp/tmp2

rm /tmp/tmp2



#FILES IN $gene/$alimethod

cp   $dir/$codeml_dir/$gene/original_alignment/codeml/fasta_renamed/$gene.$i  $dir/codeml_projects/$gene.$i/$alimethod/aligned.fasta

#aligned.prot.aln and aligned.prot.fasta

cp $dir/codeml_projects/$gene.$i/$alimethod/aligned.fasta $dir/codeml_projects/$gene.$i/$alimethod/aligned.prot.tmp1.fasta

docker run --rm -v $docker_dir/codeml_projects/$gene.$i/$alimethod:/data pegi3s/tcoffee bash -c "t_coffee -other_pg seq_reformat -in /data/aligned.prot.tmp1.fasta -action +translate -output fasta -out /data/aligned.prot.tmp2.fasta"
rm $dir/codeml_projects/$gene.$i/$alimethod/aligned.prot.tmp1.fasta

docker run --rm -v $docker_dir/codeml_projects/$gene.$i/$alimethod:/data pegi3s/alter -i /data/aligned.prot.tmp2.fasta -o /data/aligned.prot.aln -ia -of ALN -oo Linux -op GENERAL &> /dev/null

docker run --rm -e USERID=$UID -e USER=$USER -e DISPLAY=$DISPLAY -v /var/db:/var/db:Z -v /tmp/.X11-unix:/tmp/.X11-unix -v $HOME/.Xauthority:/home/developer/.Xauthority -v "$docker_dir/codeml_projects/$gene.$i/$alimethod:/data" -v /var/run/docker.sock:/var/run/docker.sock -v /tmp:/tmp pegi3s/seda:1.6.0-v2304 /opt/SEDA/run-cli.sh reformat -if /data/aligned.prot.tmp2.fasta -od /data -rlb &> /dev/null

mv $dir/codeml_projects/$gene.$i/$alimethod/aligned.prot.tmp2.fasta $dir/codeml_projects/$gene.$i/$alimethod/aligned.prot.fasta

touch $dir/codeml_projects/$gene.$i/$alimethod/project.conf

#aligned.score_ascii
docker run --rm -v $docker_dir/codeml_projects/$gene.$i/$alimethod:/data pegi3s/tcoffee:12.00.7 t_coffee /data/aligned.prot.fasta -method=muscle_msa -output=score_ascii -run_name /data/aligned &> /dev/null
rm /data/codeml_projects/$gene.$i/$alimethod/aligned.dnd

#codeml.out
cp $dir/$codeml_dir/$gene/$codeml_results/$gene.$i/$gene.$i.codeml.out $dir/codeml_projects/$gene.$i/$alimethod/codeml.out



#codeml.sum
sed -e '/Model 1/,/Note: Branch length/!d' $dir/codeml_projects/$gene.$i/$alimethod/codeml.out > $dir/codeml_projects/$gene.$i/$alimethod/tmp1
sed -e '/Model 2/,/Note: Branch length/!d' $dir/codeml_projects/$gene.$i/$alimethod/codeml.out >> $dir/codeml_projects/$gene.$i/$alimethod/tmp1
sed -e '/Model 0/,/Note: Branch length/!d' $dir/codeml_projects/$gene.$i/$alimethod/codeml.out >> $dir/codeml_projects/$gene.$i/$alimethod/tmp1
sed -e '/Model 3/,/Note: Branch length/!d' $dir/codeml_projects/$gene.$i/$alimethod/codeml.out >> $dir/codeml_projects/$gene.$i/$alimethod/tmp1
sed -e '/Model 7/,/Note: Branch length/!d' $dir/codeml_projects/$gene.$i/$alimethod/codeml.out >> $dir/codeml_projects/$gene.$i/$alimethod/tmp1
sed -e '/Model 8/,/Note: Branch length/!d' $dir/codeml_projects/$gene.$i/$alimethod/codeml.out >> $dir/codeml_projects/$gene.$i/$alimethod/tmp1
grep 'lnL\|Model' $dir/codeml_projects/$gene.$i/$alimethod/tmp1 > $dir/codeml_projects/$gene.$i/$alimethod/tmp2
rm $dir/codeml_projects/$gene.$i/$alimethod/tmp1
sed -i  's/one-ratio/one-ratio dum /g' $dir/codeml_projects/$gene.$i/$alimethod/tmp2
tr '\n' ' ' < $dir/codeml_projects/$gene.$i/$alimethod/tmp2 > $dir/codeml_projects/$gene.$i/$alimethod/tmp3 && rm $dir/codeml_projects/$gene.$i/$alimethod/tmp2
sed 's/Model/\nModel/g' $dir/codeml_projects/$gene.$i/$alimethod/tmp3 > $dir/codeml_projects/$gene.$i/$alimethod/tmp4 && rm $dir/codeml_projects/$gene.$i/$alimethod/tmp3
sed -i -e "s/([a-z,A-Z, ,0-9,:]*)//g" $dir/codeml_projects/$gene.$i/$alimethod/tmp4
tr -s " " <  $dir/codeml_projects/$gene.$i/$alimethod/tmp4 >  $dir/codeml_projects/$gene.$i/$alimethod/tmp5 && rm $dir/codeml_projects/$gene.$i/$alimethod/tmp4
sed -i 's/ lnL: /\t/g' $dir/codeml_projects/$gene.$i/$alimethod/tmp5
cut -f1-3 -d ' ' $dir/codeml_projects/$gene.$i/$alimethod/tmp5 | grep . > $dir/codeml_projects/$gene.$i/$alimethod/codeml.sum
rm $dir/codeml_projects/$gene.$i/$alimethod/tmp5
a0=$(grep 'Model 0' $dir/codeml_projects/$gene.$i/$alimethod/codeml.sum | cut -f2 -d$'\t' )
a1=$(grep 'Model 1' $dir/codeml_projects/$gene.$i/$alimethod/codeml.sum | cut -f2 -d$'\t' )
a2=$(grep 'Model 2' $dir/codeml_projects/$gene.$i/$alimethod/codeml.sum | cut -f2 -d$'\t' )
a7=$(grep 'Model 7' $dir/codeml_projects/$gene.$i/$alimethod/codeml.sum | cut -f2 -d$'\t' )
a8=$(grep 'Model 8' $dir/codeml_projects/$gene.$i/$alimethod/codeml.sum | cut -f2 -d$'\t' )
if grep -q 'Model 0' $dir/codeml_projects/$gene.$i/$alimethod/codeml.sum && grep -q 'Model 1' $dir/codeml_projects/$gene.$i/$alimethod/codeml.sum; then
    a01=$(echo "2 * ($a1 - $a0)" | bc)
    echo -e "\n\nModel 0 vs 1\t"$a01 >> $dir/codeml_projects/$gene.$i/$alimethod/codeml.sum
fi
if grep -q 'Model 2' $dir/codeml_projects/$gene.$i/$alimethod/codeml.sum && grep -q 'Model 1' $dir/codeml_projects/$gene.$i/$alimethod/codeml.sum; then
    a21=$(echo "2 * ($a2 - $a1)" | bc)
    echo -e "\nModel 2 vs 1\t"$a21 >> $dir/codeml_projects/$gene.$i/$alimethod/codeml.sum    
    testM2=$(echo "$a21 > 5.99" |bc)
    if [ $testM2 -eq 1 ]; then
        echo -e "\nAdditional information for M1 vs M2:" >> $dir/codeml_projects/$gene.$i/$alimethod/codeml.sum
        awk '/Model 2/,/p0-p1 /' $dir/codeml_projects/$gene.$i/$alimethod/codeml.out | awk '/Naive/,/The grid/' | head -n -4 >> $dir/codeml_projects/$gene.$i/$alimethod/codeml.sum
    fi
fi
if grep -q 'Model 8' $dir/codeml_projects/$gene.$i/$alimethod/codeml.sum && grep -q 'Model 7' $dir/codeml_projects/$gene.$i/$alimethod/codeml.sum; then
    a87=$(echo "2 * ($a8 - $a7)" | bc)
    echo -e "\n\nModel 8 vs 7\t"$a87 >> $dir/codeml_projects/$gene.$i/$alimethod/codeml.sum
    testM8=$(echo "$a87 > 5.99" |bc)
    if [ $testM8 -eq 1 ]; then
        echo -e "\nAdditional information for M7 vs M8:" >> $dir/codeml_projects/$gene.$i/$alimethod/codeml.sum
        awk '/Model 8/,/The grid/' $dir/codeml_projects/$gene.$i/$alimethod/codeml.out | awk '/Naive/,/The grid/' | head -n -4 >> $dir/codeml_projects/$gene.$i/$alimethod/codeml.sum
    fi
fi
echo "" >> $dir/codeml_projects/$gene.$i/$alimethod/codeml.sum



#input.fasta
cp $dir/$codeml_dir/$gene/$codeml_oa_dir/$gene.$i $dir/codeml_projects/$gene.$i/$alimethod/input.fasta
sed -i 's/-//g' $dir/codeml_projects/$gene.$i/$alimethod/input.fasta



#mrbayes.log.psrf
cp $dir/codeml_projects/$gene.$i/$alimethod/allfiles/mrbayes/mrbayes.log.psrf $dir/codeml_projects/$gene.$i/$alimethod/mrbayes.log.psrf



#names.txt
cp $dir/codeml_projects/$gene.$i/names.txt $dir/codeml_projects/$gene.$i/$alimethod/names.txt

#notes.txt
echo "Not all of the following information may be relevant for the case being handled, since this project may be part of a much larger auto-PSS-genome project where several methods of detection of positively selected sites have been used. As such the aligned.score_ascii file may have more sequences than the file effectively used to detect positively selected codons, since the content of this file reflects the content of the file used for the master alignment, from which a subsample may have been taken." > $dir/codeml_projects/$gene.$i/$alimethod/notes.tmp1
echo "" >> $dir/codeml_projects/$gene.$i/$alimethod/notes.tmp1
cat $dir/codeml_projects/$gene.$i/$alimethod/notes.tmp1 $dir/ipssa-project.params > $dir/codeml_projects/$gene.$i/$alimethod/notes.txt && rm $dir/codeml_projects/$gene.$i/$alimethod/notes.tmp1


#phipack.log
cp $dir/$phipack_dir/$gene/original_alignment/codeml/phipack/$gene.$i/phipack.log $dir/codeml_projects/$gene.$i/$alimethod/phipack.log

#tree.con
cp $dir/codeml_projects/$gene.$i/$alimethod/allfiles/mrbayes/input.fasta.fasta.mrb.con $dir/codeml_projects/$gene.$i/$alimethod/tree.con
while read name; do
	rename_a=$(echo $name | cut -f3 -d' ')
	rename_b=$(echo $name | cut -f1 -d' ')
	sed -i "s/\t$rename_a$/\t$rename_b/g" $dir/codeml_projects/$gene.$i/$alimethod/tree.con
	sed -i "s/\t$rename_a\,$/\t$rename_b\,/g" $dir/codeml_projects/$gene.$i/$alimethod/tree.con
done < $dir/codeml_projects/$gene.$i/$alimethod/names.txt

#output.sum
echo "--- EXPERIMENT NOTES" > $dir/codeml_projects/$gene.$i/$alimethod/output.sum.tmp1
cat $dir/codeml_projects/$gene.$i/$alimethod/output.sum.tmp1 $dir/codeml_projects/$gene.$i/$alimethod/notes.txt > $dir/codeml_projects/$gene.$i/$alimethod/output.sum.tmp2 && rm $dir/codeml_projects/$gene.$i/$alimethod/output.sum.tmp1
echo "" >> $dir/codeml_projects/$gene.$i/$alimethod/output.sum.tmp2
echo "" >> $dir/codeml_projects/$gene.$i/$alimethod/output.sum.tmp2
echo "--- PSRF SUMMARY" >> $dir/codeml_projects/$gene.$i/$alimethod/output.sum.tmp2
cat $dir/codeml_projects/$gene.$i/$alimethod/output.sum.tmp2 $dir/codeml_projects/$gene.$i/$alimethod/mrbayes.log.psrf  > $dir/codeml_projects/$gene.$i/$alimethod/output.sum.tmp3 && rm $dir/codeml_projects/$gene.$i/$alimethod/output.sum.tmp2
echo "" >> $dir/codeml_projects/$gene.$i/$alimethod/output.sum.tmp3
echo "" >> $dir/codeml_projects/$gene.$i/$alimethod/output.sum.tmp3
echo "--- CODEML SUMMARY" >> $dir/codeml_projects/$gene.$i/$alimethod/output.sum.tmp3
cat $dir/codeml_projects/$gene.$i/$alimethod/output.sum.tmp3 $dir/codeml_projects/$gene.$i/$alimethod/codeml.sum  > $dir/codeml_projects/$gene.$i/$alimethod/output.sum && rm $dir/codeml_projects/$gene.$i/$alimethod/output.sum.tmp3

#input.fasta.fasta.out.sum
cp $dir/codeml_projects/$gene.$i/$alimethod/codeml.sum $dir/codeml_projects/$gene.$i/$alimethod/allfiles/codeml/input.fasta.fasta.out.sum

#output.log
s0=$(grep -l $gene $dir/ipssa_project/pipeline_working_dir/logs/align-protein-sequences*.out.log)
s1=$(grep -l $gene $dir/ipssa_project/pipeline_working_dir/logs/mrbayes-filter-alignment*.out.log)
s2=$(echo $gene"/gapped_alignment/codeml")
s3=$(grep -l $s2 $dir/ipssa_project/pipeline_working_dir/logs/run-mrbayes*.out.log)
s4=$(echo $gene"/original_alignment/codeml")
s5=$(grep -l $s4 $dir/ipssa_project/pipeline_working_dir/logs/run-codeml*.out.log)
cat $s0 $s1 $s3 $s0 $s5 > /tmp/log.tmp1
mv  /tmp/log.tmp1 $dir/codeml_projects/$gene.$i/$alimethod/output.log

cd $dir

done < /tmp/tmp1
done

rm /tmp/tmp1

#prepare tar file
cd $dir/codeml_projects && ls > names_list && sed -i 's/names_list//g' names_list
while read name; do
     tar -czvf $name.tar.gz $name > /dev/null 2>&1
done < $dir/codeml_projects/names_list
rm $dir/codeml_projects/names_list
echo "Please note that zip file names must be under 25 characters to submit to B+"
chmod -R 777 $dir
