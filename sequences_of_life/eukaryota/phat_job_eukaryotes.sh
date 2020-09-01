#!/bin/bash

#SBATCH --partition=batch
#SBATCH --nodes=1
#SBATCH --nodelist=
#SBATCH --ntasks-per-node=20
#SBATCH --job-name="phat"
#SBATCH --output=phat.output
#SBATCH --mail-user=haris.zafr@gmail.com
#SBATCH --mail-type=ALL
#SBATCH --requeue




## Running PhAT asking for 1000 consensus sequences (by default)
#/home1/haris/Desktop/stsm/sequences_of_life/gappa/bin/gappa prepare phat --taxonomy-file second_atte
mpt/taxonomies_of_the_final_seqs_with_species.txt \
#--sequence-file second_attempt/final_alignment_for_eukaryotes_with_species.fasta --target-size 1000 
--threads 20 \
#--consensus-method majorities --out-dir second_attempt/phat_final_alignment

# Setting the order level as min-tax-tevel
/home1/haris/Desktop/stsm/sequences_of_life/gappa/bin/gappa prepare phat --taxonomy-file second_attem
pt/taxonomies_of_the_final_seqs_with_species.txt \
--sequence-file second_attempt/final_alignment_for_eukaryotes_with_species.fasta --target-size 1000 -
-min-tax-level 3 --threads 20 \
--consensus-method majorities --out-dir second_attempt/phat_final_alignment
