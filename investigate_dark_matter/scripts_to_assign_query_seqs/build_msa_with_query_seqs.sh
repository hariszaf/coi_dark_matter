#!/bin/bash

#SBATCH --partition=minibatch
#SBATCH --nodes=1
#SBATCH --nodelist=
#SBATCH --ntasks-per-node=12
#SBATCH --mem=

#SBATCH --job-name="papara"
#SBATCH --output=papara.output
#SBATCH --mail-user=haris.zafr@gmail.com
#SBATCH --mail-type=ALL
#SBATCH --requeue



/home1/haris/programs/papara_nt-2.5/papara \
-t ../../build_tree_of_life/alternative_built/fast_Tree.raxml.bestTree \
-s ../../build_tree_of_life/alternative_built/all_consensus_aligned3__removed.fasta.raxml.reduced.phy \
-q ../processed_query_sequences/marine/marine_query_short_dark_matter_top6_multilne_labeled.fasta \
-n TEST_papara_output \
-r \
-j 12

