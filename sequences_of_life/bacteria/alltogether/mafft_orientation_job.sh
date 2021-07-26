#!/bin/bash

#SBATCH -N 3
#SBATCH -B 3:10:1
#SBATCH --partition=batch

#SBATCH --ntasks-per-node=15
#SBATCH --cpus-per-task=1
#SBATCH --hint=compute_bound
#SBATCH --job-name="allBac"

#SBATCH --output=bac_all_orient.output
#SBATCH --mail-user=haris.zafr@gmail.com
#SBATCH --mail-type=ALL
#SBATCH --requeue


export MAFFT_N_THREADS_PER_PROCESS="1"
export MAFFT_MPIRUN="/usr/bin/mpirun.openmpi -n 45 -npernode 15 -bind-to none"

/mnt/big/Tools/mafft-7.453-with-extensions/bin/mafft \
--mpi \
--thread 15 \
--globalpair \
--adjustdirectionaccurately \
all_bacteria_cox1.fasta > aligned_all_bacteria_cox1.fasta
