#!/bin/bash 

#SBATCH --partition=batch
###SBATCH --nodes=
#SBATCH --nodelist=
#SBATCH --ntasks-per-node=4
#SBATCH --mem=
# Memory per node specification is in MB. It is optional.
# The default limit is 3000MB per core.
#SBATCH --job-name="archaea"
#SBATCH --output=archaea.output
#SBATCH --mail-user=haris.zafr@gmail.com
#SBATCH --mail-type=ALL
#SBATCH --requeue


/mnt/big/Phylogeny/iqtree-2.0-rc1-Linux/bin/iqtree \
-s ../consensus_seqs/../consensus_seqs/archaea_consensus.fasta \
-m  MFP \
-alrt 1000 \
-B 1000 \
--prefix archaeaTree \
-T AUTO



# -b specifies the number of bootstrap replicates where 100 is the minimum recommended number.
# -B specifies the number of bootstrap replicates where 1000 is the minimum number recommended.
# -alrt specifies the number of bootstrap replicates for SH-aLRT where 1000 is the minimum number recommended.

# IQ-TREE 2 provides fast and parallel implementations for several existing branch tests including the 
# approximate likelihood ratio test (aLRT) 

# the Shimodaira–Hasegawa-like aLRT (SH-aLRT)


