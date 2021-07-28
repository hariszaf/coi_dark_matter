#!/usr/bin/python3.5

import sys

input_file = open("all_bacteria_cox1_singleline.fasta","r")
output_file = open("output_longest_bacteria.fasta", "w+")


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


keep_seqs = {}

# SET THE NUMBER OF LONGEST SEQS YOU NEED
for i in range(400):
    keymax = max(titles_lengths, key=titles_lengths.get)
    keep_seqs[keymax] = titles_seq[keymax]
    del titles_seq[keymax]
    del titles_lengths[keymax]

    
for key, value in keep_seqs.items():
    output_file.write(key + value + "\n")

output_file.close()
