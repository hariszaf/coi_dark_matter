#!/bin/bash

#SBATCH --partition=minibatch
#SBATCH --nodes=1
#SBATCH --nodelist=
#SBATCH --ntasks-per-node=12
#SBATCH --mem=
# Memory per node specification is in MB. It is optional.
# The default limit is 3000MB per core.
#SBATCH --job-name="papara"
#SBATCH --output=papara.output
#SBATCH --mail-user=haris.zafr@gmail.com
#SBATCH --mail-type=ALL
#SBATCH --requeue





#/home1/haris/metabar_pipeline/PEMA/tools/papara_static_x86_64 \
/home1/haris/Desktop/test_papara/papara_nt/papara \
-t /home1/haris/Desktop/test_papara/dark_coi/bestML_tree.tree \
-s /home1/haris/Desktop/test_papara/dark_coi/all_consensus_aligned.fasta.phylip \
-n mock \
-q /home1/haris/Desktop/dark_matter/investigate_dark_matter/processed_query_sequences/mock/mock_seqs.fasta \
-r \
-j 12


