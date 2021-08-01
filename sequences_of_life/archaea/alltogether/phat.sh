#!/bin/bash

#SBATCH --partition=batch
#SBATCH --nodes=1
#SBATCH --nodelist=
#SBATCH --ntasks-per-node=20
#SBATCH --job-name="phatArc"
#SBATCH --output=phat_arch.output
#SBATCH --mail-user=haris.zafr@gmail.com
#SBATCH --mail-type=ALL
#SBATCH --requeue


# Setting the order level as min-tax-tevel
/home1/haris/Desktop/stsm/sequences_of_life/gappa/bin/gappa prepare phat --taxonomy-file taxonomies_present.tsv \
    --sequence-file trimmed_aligned_archaea.aln \
    --target-size 23  \
    --min-tax-level 5 \
    --threads 20 \
    --consensus-method majorities \
    --out-dir phat_archaea_lev_5

