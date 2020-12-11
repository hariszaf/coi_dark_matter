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
#/home1/haris/Desktop/stsm/sequences_of_life/gappa/bin/gappa prepare phat   \
#--taxonomy-file taxonomies_for_phat_final.tsv \
#--sequence-file full_midori_alignment_no_taxon_levels_extra_codes_removed_no_tabs.aln \
#--target-size 1000 \
#--threads 20 \
#--consensus-method majorities \
#--out-dir phat_output

# Setting the order level as min-tax-tevel
/home1/haris/Desktop/stsm/sequences_of_life/gappa/bin/gappa prepare phat \
--taxonomy-file taxonomies_for_phat_final.tsv \
--sequence-file full_midori_alignment_no_taxon_levels_extra_codes_removed_no_tabs.aln \
--target-size 1000 \
--min-tax-level 4 \
--threads 20 \
--consensus-method majorities \
--out-dir phat_output




