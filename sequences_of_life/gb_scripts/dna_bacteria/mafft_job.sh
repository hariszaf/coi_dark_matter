#!/bin/bash

#SBATCH --partition=batch
#SBATCH --nodes=1
#SBATCH --nodelist=
#SBATCH --ntasks-per-node=20
#SBATCH --mem=
# Memory per node specification is in MB. It is optional.
# The default limit is 3000MB per core.
#SBATCH --job-name="bact-mafft"
#SBATCH --output=bacteria_mafft.output
#SBATCH --mail-user=haris.zafr@gmail.com
#SBATCH --mail-type=ALL
#SBATCH --requeue


/usr/bin/mafft --thread 20 --globalpair bacteria_sequences_taxonomy.fasta > aligned_bacteria_sequences.fasta
