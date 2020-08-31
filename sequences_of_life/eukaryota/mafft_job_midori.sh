#!/bin/bash

#SBATCH -N 2
#SBATCH -B 2:10:1
#SBATCH --partition=batch

#SBATCH --ntasks-per-node=15
#SBATCH --cpus-per-task=1
#SBATCH --hint=compute_bound
#SBATCH --job-name="mpialt"

#SBATCH --output=mafft-midori-fast.output
#SBATCH --mail-user=haris.zafr@gmail.com
#SBATCH --mail-type=ALL
#SBATCH --requeue




export MAFFT_N_THREADS_PER_PROCESS="1"
export MAFFT_MPIRUN="/usr/bin/mpirun -n 30 -npernode 15 -bind-to none"


export MAFFT_N_THREADS_PER_PROCESS="1"
export MAFFT_MPIRUN="/usr/bin/mpirun -n 30 -npernode 15 -bind-to none"

/mnt/big/Tools/mafft-7.453-with-extensions/bin/mafft \
--mpi \
--large \
--globalpair \
--thread 15 \
MIDORI_single_species_input_for_mafft.fasta > \
MIDORI_alignment.fasta
