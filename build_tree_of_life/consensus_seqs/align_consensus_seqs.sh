#!/bin/bash

#SBATCH --job-name="consensus_msa"
#SBATCH --output=consensus_align_alt.output
#SBATCH --mail-type=ALL
#SBATCH --requeue
#SBATCH -p batch
#SBATCH -N 3
#SBATCH --ntasks-per-node=15
#SBATCH --mail-user=haris.zafr@gmail.com



export MAFFT_N_THREADS_PER_PROCESS="1"
export MAFFT_MPIRUN="/usr/bin/mpirun.openmpi -n 45 -npernode 15 -bind-to none"

export MAFFT_N_THREADS_PER_PROCESS="1"
export MAFFT_MPIRUN="/usr/bin/mpirun.openmpi -n 45 -npernode 15 -bind-to none"


mpirun.openmpi  /mnt/big/Tools/mafft-7.453-with-extensions/bin/mafft --mpi \
   --globalpair \
   --adjustdirectionaccurately \
   --maxiterate 1000 \
   non_period_all_seqs_multileline.fasta >  all_consensus_aligned_adjust_dir.aln


# Run the mafft alignment tool
#/usr/bin/mafft --globalpair --maxiterate 1000 --thread 20 consensus_sequences/all_consensus_mafft_input.fasta >  all_consensus_aligned.fasta

