#!/usr/bin/python3.5

all_seqs_file = open("MIDORI_single_species_input_for_mafft_single_line.fasta","r")
core_seqs_file = open("core_seqs_aln_singleline.fasta", "r")
output_file = open("rest_midori_seqs.fasta", "w+")


# Keep titles of the sequences of core
core_seqs = []
for line in core_seqs_file:
    if line[0] == ">":
        core_seqs.append(line)
    else:
        continue


# Keep a dictionary with keys the title and value the sequence for all the midori unique seqs
all_seqs_dic = {}
for line in all_seqs_file:
    if line[0] == ">":
        title = line
    else:
        all_seqs_dic[title] = line

# Write in a file only those seqs that are not in the core
for title, seq in all_seqs_dic.items():
    
    if title not in core_seqs:
        
        output_file.write(title + seq + "\n")
        
    else:        
        continue

    
    
