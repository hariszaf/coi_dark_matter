#!/bin/bash -l

#SBATCH --partition=batch
#SBATCH --nodes=1
#SBATCH --nodelist=
#SBATCH --ntasks-per-node=20
#SBATCH --mem=
# Memory per node specification is in MB. It is optional.
# The default limit is 3000MB per core.
#SBATCH --job-name="consensus_msa"
#SBATCH --output=consensus_msa.output
#SBATCH --mail-user=haris.zafr@gmail.com
#SBATCH --mail-type=ALL
#SBATCH --requeue


# Load the mafft module on the Zorbas HPC system and start time 
module purge # unloads all previous loads
module load mafft/7.453
start=$SECONDS


# Run the mafft alignment tool
/usr/bin/mafft --globalpair --maxiterate 1000 --thread 20 consensus_sequences/all_consensus_mafft_input.fasta >  all_consensus_aligned.fasta


# Stop counting the time and unload the environment module 
duration=$(( SECONDS - start ))
echo "duration is : $duration  "
module unload mafft/7.453 #unloads mafft
