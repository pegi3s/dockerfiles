#!/bin/bash

echo "Running....."

docker_dir=$1
dir=/data
rh_dir=/ipssa_project/pipeline_working_dir/input/3_renamed_headers
ma_dir=/ipssa_project/pipeline_working_dir/input/8_master_alignment
mar_dir=/ipssa_project/pipeline_working_dir/input/9_master_alignment_renamed
omegamap_dir=/ipssa_project/pipeline_working_dir/pss_subsets
omegamap_oa_dir=/original_alignment/omegamap/fasta
omegamap_results=/original_alignment/omegamap/results/
tcoffee_dir=/ipssa_project/pipeline_working_dir/input/6_aligned
phipack_dir=/ipssa_project/pipeline_working_dir/pss_subsets

alimethod=$(grep "align_method=" $dir/ipssa-project.params  | cut -f2 -d'=') 
cd $dir/$ma_dir && ls > /tmp/tmp1

START=1
END=$(grep "omegamap_runs=" $dir/ipssa-project.params  | cut -f2 -d'=')
for i in $(eval echo "{$START..$END}")
do

while read gene
do

			   
mkdir -p $dir/omegamap_projects/$gene.$i/$alimethod/

chmod -R 777 $dir/omegamap_projects/



#FILES IN $gene

#input.fasta
cp $dir/$omegamap_dir/$gene/$omegamap_oa_dir/$gene.$i $dir/omegamap_projects/$gene.$i/input.fasta


#names.txt
cp $dir/$rh_dir/$gene.headers_map $dir/omegamap_projects/$gene.$i/names_tmp.txt
 						
awk '{ print $2 "\t" $1}' $dir/omegamap_projects/$gene.$i/names_tmp.txt | sed 's/>//g; s/\t/ - /g' > $dir/omegamap_projects/$gene.$i/names.txt
		     
rm $dir/omegamap_projects/$gene.$i/names_tmp.txt


#empty project.conf
touch $dir/omegamap_projects/$gene.$i/project.conf





#FILES IN $gene/$alimethod

gene_mod=$(echo $gene | sed 's/\.result//g')

#aligned.fasta
cp $dir/$mar_dir/$gene $dir/omegamap_projects/$gene.$i/$alimethod/aligned.fasta



#aligned.prot.aln
cp $dir/$tcoffee_dir/$gene_mod.aln $dir/omegamap_projects/$gene.$i/$alimethod/aligned.prot.aln

cp $dir/$rh_dir/$gene.headers_map $dir/omegamap_projects/$gene.$i/$alimethod/tmp2

sed -i 's/>//g' $dir/omegamap_projects/$gene.$i/$alimethod/tmp2

cd $dir/omegamap_projects/$gene.$i/$alimethod/

while read field1 field2
do

sed -i "s/$field1/$field2/g" aligned.prot.aln

done < tmp2

rm $dir/omegamap_projects/$gene.$i/$alimethod/tmp2



#aligned.prot.fasta
cp $dir/$tcoffee_dir/$gene_mod.fasta_aln $dir/omegamap_projects/$gene.$i/$alimethod/input.fasta.fasta.prot_tmp.fasta

cp $dir/$rh_dir/$gene.headers_map $dir/omegamap_projects/$gene.$i/$alimethod/$gene.headers_map.tmp

docker run --rm -v $docker_dir/omegamap_projects/$gene.$i/$alimethod/:/data pegi3s/utilities:latest fasta_put_headers_back /data/input.fasta.fasta.prot_tmp.fasta /data/$gene.headers_map.tmp /data/aligned.prot.fasta

rm $dir/omegamap_projects/$gene.$i/$alimethod/input.fasta.fasta.prot_tmp.fasta

rm $dir/omegamap_projects/$gene.$i/$alimethod/$gene.headers_map.tmp

#aligned.score_ascii
docker run --rm -v $docker_dir/omegamap_projects/$gene.$i/$alimethod:/data pegi3s/tcoffee:12.00.7 t_coffee /data/aligned.prot.fasta -method=muscle_msa -output=score_ascii -run_name /data/aligned &> /dev/null
rm /data/omegamap_projects/$gene.$i/$alimethod/aligned.dnd



#input.fasta	
cp $dir/$omegamap_dir/$gene/$omegamap_oa_dir/$gene.$i $dir/omegamap_projects/$gene.$i/$alimethod/input.fasta



#names.txt
cp $dir/omegamap_projects/$gene.$i/names.txt $dir/omegamap_projects/$gene.$i/$alimethod/names.txt



#notes.txt
echo "Not all of the following information may be relevant for the case being handled, since this project may be part of a much larger auto-PSS-genome project where several methods of detection of positively selected sites have been used. As such the aligned.score_ascii file may have more sequences than the file effectively used to detect positively selected codons, since the content of this file reflects the content of the file used for the master alignment, from which a subsample may have been taken" > $dir/omegamap_projects/$gene.$i/$alimethod/notes.tmp1
echo "" >> $dir/omegamap_projects/$gene.$i/$alimethod/notes.tmp1
cat $dir/omegamap_projects/$gene.$i/$alimethod/notes.tmp1 $dir/ipssa-project.params > $dir/omegamap_projects/$gene.$i/$alimethod/notes.txt && rm $dir/omegamap_projects/$gene.$i/$alimethod/notes.tmp1

#omegamap.sum
cp $dir/$omegamap_dir/$gene/$omegamap_results/$gene.$i/$gene.$i.summary $dir/omegamap_projects/$gene.$i/$alimethod/omegamap.sum



#phipack.log
cp $dir/$phipack_dir/$gene/original_alignment/omegamap/phipack/$gene.$i/phipack.log $dir/omegamap_projects/$gene.$i/$alimethod/phipack.log


#output.log
s1=$(grep -l $gene $dir/ipssa_project/pipeline_working_dir/logs/align-protein-sequences*.out.log)
s2=$(echo $gene"/original_alignment/omegamap")
s3=$(grep -l $s2 $dir/ipssa_project/pipeline_working_dir/logs/run-omegamap*.out.log)
cat $s1 $s3 > /tmp/log.tmp1
mv  /tmp/log.tmp1 $dir/omegamap_projects/$gene.$i/$alimethod/output.log

cd $dir

done < /tmp/tmp1
done

rm /tmp/tmp1

#prepare tar file
cd $dir/omegamap_projects && ls > names_list && sed -i 's/names_list//g' names_list
while read name; do
     tar -czvf $name.tar.gz $name > /dev/null 2>&1
done < $dir/omegamap_projects/names_list
rm $dir/omegamap_projects/names_list
echo "Please note that zip file names must be under 25 characters to submit to B+"
chmod -R 777 $dir
