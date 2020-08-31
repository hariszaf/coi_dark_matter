#!/bin/bash

#SBATCH --partition=batch
#SBATCH --nodes=1
#SBATCH --nodelist=
#SBATCH --ntasks-per-node=20
#SBATCH --mem=
# Memory per node specification is in MB. It is optional.
# The default limit is 3000MB per core.
#SBATCH --job-name="phat"
#SBATCH --output=phat.output
#SBATCH --mail-user=haris.zafr@gmail.com
#SBATCH --mail-type=ALL
#SBATCH --requeue


/home1/haris/Desktop/stsm/sequences_of_life/gappa/bin/gappa prepare phat --taxonomy-file taxonomies_for_phat.tsv \
--sequence-file aligned_bacteria_sequences_true_orientation.fasta \
--target-size 70 \
--min-tax-level 3 \
--out-dir /home1/haris/Desktop/stsm/sequences_of_life/bacteria/phat_output
