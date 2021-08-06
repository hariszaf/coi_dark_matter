#!/bin/bash

#SBATCH -N 1
#SBATCH --partition=batch

#SBATCH --ntasks-per-node=20
#SBATCH --cpus-per-task=1
#SBATCH --hint=compute_bound
#SBATCH --job-name="archPfam"

#SBATCH --output=arch_pfam.output
#SBATCH --mail-user=haris.zafr@gmail.com
#SBATCH --mail-type=ALL
#SBATCH --requeue



/mnt/big/Tools/mafft-7.453-with-extensions/bin/mafft \
--mpi \
--thread 20 \
--globalpair \
--adjustdirectionaccurately \
pfam_archaea.fasta > aligned_pfam_archaea.fasta
