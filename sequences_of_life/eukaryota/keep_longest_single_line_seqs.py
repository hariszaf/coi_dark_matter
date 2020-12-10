#!/usr/bin/python3.5

import sys

input_file = open("MIDORI_single_species_input_for_mafft_single_line.fasta","r")
output_file = open("longest_500_single_line_seqs.fasta", "w+")

titles_seq = {}
titles_lengths = {}

counter = 0


for line in input_file:
    
    if line[0] == ">" :
        title = line
        
    else:
        titles_lengths[title] = len(line)
        titles_seq[title] = line
        counter += 1
input_file.close()    

print("i am about to count to 500\n")

keep_seqs = {}
for i in range(500):
    keymax = max(titles_lengths, key=titles_lengths.get)
    keep_seqs[keymax] = titles_seq[keymax]
    del titles_seq[keymax]
    del titles_lengths[keymax]
    print(i)

    
for key, value in keep_seqs.items():
    output_file.write(key + value + "\n")

output_file.close()