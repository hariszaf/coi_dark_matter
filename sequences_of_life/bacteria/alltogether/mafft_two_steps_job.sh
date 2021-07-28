#!/bin/bash

#SBATCH --partition=batch
#SBATCH --nodes=1
#SBATCH --nodelist=
#SBATCH --ntasks-per-node=20
#SBATCH --mem=
# Memory per node specification is in MB. It is optional.
# The default limit is 3000MB per core.
#SBATCH --job-name="twoStepsMafft"
#SBATCH --output=step_2_mafft.output
#SBATCH --mail-user=haris.zafr@gmail.com
#SBATCH --mail-type=ALL
#SBATCH --requeue



## Core alignment
#/mnt/big/Tools/mafft-7.453-with-extensions/bin/mafft --auto --reorder core_seqs.fasta  > core_bacteria_alignment.aln


# Alignment of the rest of the sequences based on the first one
/mnt/big/Tools/mafft-7.453-with-extensions/bin/mafft --thread 20 --auto --addfull rest_bacteria_seqs.fasta --keeplength --reorder core_bacteria_alignment.aln >  bacteria_alignment.aln

