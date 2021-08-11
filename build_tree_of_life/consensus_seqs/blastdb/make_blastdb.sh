#!/bin/bash


# Move all blastable .fasta files from the multiple databases used here
cat ../non_period_all_seqs_singleline.fasta > coi_ref_seqs.fasta.tmp

# Check if there are non-sequences entries
awk 'BEGIN{RS=">"} $2~/^[A-Z]+$/ {print ">"$0}' coi_ref_seqs.fasta.tmp > coi_ref_seqs.fasta
rm coi_ref_seqs.fasta.tmp

# should be invoked from: /data/databases/sequence_databases/prego_ref_seq_db by the prego user
# makeblastdb -in /data/databases/sequence_databases/silva/silva138/silva138_with_ncbi_tax_ids.fasta -out prego_blastdb -dbtype nucl

makeblastdb -in coi_ref_seqs.fasta -out coi_blastdb -dbtype nucl
rm coi_ref_seqs.fasta
