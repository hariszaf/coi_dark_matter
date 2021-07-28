#!/bin/bash

#SBATCH --job-name="test2"
#SBATCH --output=alternative.output
#SBATCH --mail-type=ALL
#SBATCH --requeue
#SBATCH -p batch
#SBATCH -N 2
#SBATCH --ntasks-per-node=15





export MAFFT_N_THREADS_PER_PROCESS="1"
export MAFFT_MPIRUN="/usr/bin/mpirun.openmpi -n 30 -npernode 15 -bind-to none"


export MAFFT_N_THREADS_PER_PROCESS="1"
export MAFFT_MPIRUN="/usr/bin/mpirun.openmpi -n 30 -npernode 15 -bind-to none"


mpirun.openmpi -c 30  /mnt/big/Tools/mafft-7.453-with-extensions/bin/mafft --globalpair all_bacteria_cox1.fasta > TEST_OUTPUT


#mpirun.openmpi /mnt/big/Tools/mafft-7.453-with-extensions/bin/mafft \
#--mpi \
#--large \
#--globalpair \
#--thread 15 \
#all_bacteria_cox1.fasta > TEST_OUTPUT
