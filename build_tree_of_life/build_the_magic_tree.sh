#!/bin/bash 

#SBATCH --partition=batch
#SBATCH --nodes=1
#SBATCH --nodelist=
#SBATCH --ntasks-per-node=20
#SBATCH --mem=
# Memory per node specification is in MB. It is optional.
# The default limit is 3000MB per core.
#SBATCH --job-name="magic_tree"
#SBATCH --output=magic_tree.output
#SBATCH --mail-user=haris.zafr@gmail.com
#SBATCH --mail-type=ALL
#SBATCH --requeue


# Check step 
/home1/haris/metabar_pipeline/PEMA/tools/raxml-ng/raxml-ng/bin/raxml-ng \
--check --msa all_consensus_aligned3__removed.fasta --model GTR+G4 


echo "check is over \n move to final building step "


# 4 sequences were removed after the check 
/home1/haris/metabar_pipeline/PEMA/tools/raxml-ng/raxml-ng/bin/raxml-ng --all \
--msa-format FASTA \
--msa all_consensus_aligned3__removed.fasta \
--tree pars{10} \
--bs-trees 5 \
--model GTR+FO+G4m \
--threads 3

# if tree is ok, then you can try to ask for more bootstraps for a more reliable tree
# --bs-trees 100
#   GTR+G4