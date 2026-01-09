#!/bin/bash

echo "Running....."

docker_dir=$1
dir=/data
rh_dir=/ipssa_project/pipeline_working_dir/input/3_renamed_headers
ma_dir=/ipssa_project/pipeline_working_dir/input/8_master_alignment
mar_dir=/ipssa_project/pipeline_working_dir/input/9_master_alignment_renamed
fubar_dir=/ipssa_project/pipeline_working_dir/pss_subsets
fubar_oa_dir=/original_alignment/fubar/fasta
fubar_ga_dir=/gapped_alignment/fubar/mrbayes/
fubar_results=/original_alignment/fubar/results/
tcoffee_dir=/ipssa_project/pipeline_working_dir/input/6_aligned
phipack_dir=/ipssa_project/pipeline_working_dir/pss_subsets

alimethod=$(grep "align_method=" $dir/ipssa-project.params  | cut -f2 -d'=') 
cd $dir/$ma_dir && ls > /tmp/tmp1

START=1
END=$(grep "fubar_runs=" $dir/ipssa-project.params  | cut -f2 -d'=')
for i in $(eval echo "{$START..$END}")
do

while read gene
do


mkdir -p $dir/fubar_projects/$gene.$i/$alimethod/

chmod -R 777 $dir/fubar_projects/



#FILES IN $gene

#input.fasta
cp $dir/$fubar_dir/$gene/$fubar_oa_dir/$gene.$i $dir/fubar_projects/$gene.$i/input.fasta


#names.txt
cp $dir/$rh_dir/$gene.headers_map $dir/fubar_projects/$gene.$i/names_tmp.txt

awk '{ print $2 "\t" $1}' $dir/fubar_projects/$gene.$i/names_tmp.txt | sed 's/>//g; s/\t/ - /g' > $dir/fubar_projects/$gene.$i/names.txt

rm $dir/fubar_projects/$gene.$i/names_tmp.txt


#empty project.conf
touch $dir/fubar_projects/$gene.$i/project.conf





#FILES IN $gene/$alimethod

gene_mod=$(echo $gene | sed 's/\.result//g')

#aligned.fasta
cp $dir/$mar_dir/$gene $dir/fubar_projects/$gene.$i/$alimethod/aligned.fasta



#aligned.prot.aln
cp $dir/$tcoffee_dir/$gene_mod.aln $dir/fubar_projects/$gene.$i/$alimethod/aligned.prot.aln

cp $dir/$rh_dir/$gene.headers_map $dir/fubar_projects/$gene.$i/$alimethod/tmp2

sed -i 's/>//g' $dir/fubar_projects/$gene.$i/$alimethod/tmp2

cd $dir/fubar_projects/$gene.$i/$alimethod/

while read field1 field2
do

sed -i "s/$field1/$field2/g" aligned.prot.aln

done < tmp2

rm $dir/fubar_projects/$gene.$i/$alimethod/tmp2



#aligned.prot.fasta
cp $dir/$tcoffee_dir/$gene_mod.fasta_aln $dir/fubar_projects/$gene.$i/$alimethod/input.fasta.fasta.prot_tmp.fasta

cp $dir/$rh_dir/$gene.headers_map $dir/fubar_projects/$gene.$i/$alimethod/$gene.headers_map.tmp

docker run --rm -v $docker_dir/fubar_projects/$gene.$i/$alimethod/:/data pegi3s/utilities:latest fasta_put_headers_back /data/input.fasta.fasta.prot_tmp.fasta /data/$gene.headers_map.tmp /data/aligned.prot.fasta

rm $dir/fubar_projects/$gene.$i/$alimethod/input.fasta.fasta.prot_tmp.fasta

rm $dir/fubar_projects/$gene.$i/$alimethod/$gene.headers_map.tmp

#aligned.score_ascii
docker run --rm -v $docker_dir/fubar_projects/$gene.$i/$alimethod:/data pegi3s/tcoffee:12.00.7 t_coffee /data/aligned.prot.fasta -method=muscle_msa -output=score_ascii -run_name /data/aligned &> /dev/null
rm /data/fubar_projects/$gene.$i/$alimethod/aligned.dnd


#fubar.out
cp $dir/$fubar_dir/$gene/$fubar_results/$gene.$i/$gene.$i.results $dir/fubar_projects/$gene.$i/$alimethod/fubar.out



#input.fasta
cp $dir/$fubar_dir/$gene/$fubar_oa_dir/$gene.$i $dir/fubar_projects/$gene.$i/$alimethod/input.fasta



#mrbayes.log.psrf
cd $dir/ipssa_project/pipeline_working_dir/logs && ls run-mrbayes_*[13579].out.log > /tmp/tmp3
	
while read name
do

if grep -q $gene $name; then
cp $name $dir/fubar_projects/$gene.$i/$alimethod/mrbayes_tmp.log
awk '/Estimated marginal/,/runs converge/' $dir/fubar_projects/$gene.$i/$alimethod/mrbayes_tmp.log > $dir/fubar_projects/$gene.$i/$alimethod/mrbayes.log.psrf
		
fi

done < /tmp/tmp3

rm $dir/fubar_projects/$gene.$i/$alimethod/mrbayes_tmp.log

rm /tmp/tmp3



#names.txt
cp $dir/fubar_projects/$gene.$i/names.txt $dir/fubar_projects/$gene.$i/$alimethod/names.txt



#notes.txt
echo "Not all of the following information may be relevant for the case being handled, since this project may be part of a much larger auto-PSS-genome project where several methods of detection of positively selected sites have been used. As such the aligned.score_ascii file may have more sequences than the file effectively used to detect positively selected codons, since the content of this file reflects the content of the file used for the master alignment, from which a subsample may have been taken" > $dir/fubar_projects/$gene.$i/$alimethod/notes.tmp1
echo "" >> $dir/fubar_projects/$gene.$i/$alimethod/notes.tmp1
cat $dir/fubar_projects/$gene.$i/$alimethod/notes.tmp1 $dir/ipssa-project.params > $dir/fubar_projects/$gene.$i/$alimethod/notes.txt && rm $dir/fubar_projects/$gene.$i/$alimethod/notes.tmp1



#phipack.log
cp $dir/$phipack_dir/$gene/original_alignment/fubar/phipack/$gene.$i/phipack.log $dir/fubar_projects/$gene.$i/$alimethod/phipack.log


#tree.con
cp $dir/$fubar_dir/$gene/$fubar_ga_dir/$gene.$i/mrbayes_input.nex.con.tre $dir/fubar_projects/$gene.$i/$alimethod/tree.con
while read name; do
	rename_a=$(echo $name | cut -f3 -d' ')
	rename_b=$(echo $name | cut -f1 -d' ')
	sed -i "s/\t$rename_a$/\t$rename_b/g" $dir/fubar_projects/$gene.$i/$alimethod/tree.con
	sed -i "s/\t$rename_a\,$/\t$rename_b\,/g" $dir/fubar_projects/$gene.$i/$alimethod/tree.con
done < $dir/fubar_projects/$gene.$i/$alimethod/names.txt

#output.log
s0=$(grep -l $gene $dir/ipssa_project/pipeline_working_dir/logs/align-protein-sequences*.out.log)
s1=$(grep -l $gene $dir/ipssa_project/pipeline_working_dir/logs/mrbayes-filter-alignment*.out.log)
s2=$(echo $gene"/gapped_alignment/fubar")
s3=$(grep -l $s2 $dir/ipssa_project/pipeline_working_dir/logs/run-mrbayes*.out.log)
cat $s0 $s1 $s0 $s3 > /tmp/log.tmp1
echo "Running FUBAR..." >> /tmp/log.tmp1
cat /tmp/log.tmp1  $dir/fubar_projects/$gene.$i/$alimethod/fubar.out >  /tmp/log.tmp2
mv  /tmp/log.tmp2 $dir/fubar_projects/$gene.$i/$alimethod/output.log

cd $dir

done < /tmp/tmp1
done

rm /tmp/tmp1

#prepare tar file
cd $dir/fubar_projects && ls > names_list && sed -i 's/names_list//g' names_list
while read name; do
     tar -czvf $name.tar.gz $name > /dev/null 2>&1
done < $dir/fubar_projects/names_list
rm $dir/fubar_projects/names_list
echo "Please note that zip file names must be under 25 characters to submit to B+"
chmod -R 777 $dir

