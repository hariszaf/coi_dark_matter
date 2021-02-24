#!/bin/bash 

#SBATCH --partition=batch
#SBATCH --nodes=1
#SBATCH --nodelist=
#SBATCH --ntasks-per-node=20
#SBATCH --mem=
# Memory per node specification is in MB. It is optional.
# The default limit is 3000MB per core.
#SBATCH --job-name="fastTree"
#SBATCH --output=bs_check.output
#SBATCH --mail-user=haris.zafr@gmail.com
#SBATCH --mail-type=ALL
#SBATCH --requeue


/home1/haris/programs/raxml-ng/raxml-ng/bin/raxml-ng-mpi \
--search1 \
--msa all_consensus_aligned3__removed.fasta.raxml.reduced.phy \
--model GTR+G \
--seed 2 \
--prefix fast_Tree
--threads 20
