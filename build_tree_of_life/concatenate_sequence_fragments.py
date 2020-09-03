#/usr/bin/python3.5


# REMEMBER! This script takes as input the outcome of the following sed command:
# sed 's/-//g ; /^$/d' consensus_sequences_default.fasta > tmp.fasta

import os

current_directory = os.getcwd()

tmp_file = current_directory + "/tmp.fasta"
output_file = current_directory + "/dev.output"

with open(tmp_file, "r") as f: 

	lines = f.readlines()
	num_of_lines = len(lines)


	title_sequence = {}
	single_sequence_list = []
	counter = 0 

	for line in lines:

		if counter == 0 :
			title = line

		if line[0] == ">":
			counter += 1

			if counter > 2:
				title_sequence[title] = single_sequence_list
				single_sequence_list = []

			title = line

		elif counter == num_of_lines:
			sequences_in_pieces.append(single_sequence_list)

		else:
			single_sequence_list.append(line)
			counter += 1

	with open (output_file, "w+") as g:

		for key, value in title_sequence.items():

			if len(value) > 0 :
				title = key 

				value = [x[:-1] for x in value]
				value = ''.join(value)

				n = 80
				new_value = [value[i:i+n] for i in range(0, len(value), n)]

				g.write(title)
				for segment in new_value:
					g.write(segment + "\n")
