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
    --sequence-file fixed_tax_trimmed_archaea.aln \
    --target-size 20  \
    --min-tax-level 3  \
    --threads 20 \
    --consensus-method majorities \
    --out-dir phat_archaea

