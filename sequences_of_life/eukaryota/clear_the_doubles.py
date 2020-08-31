#!/usr/bin/python3.5

input = open("MIDORI_UNIQ_GB239_CO1_RDP_no_taxids.fasta","r")
output = open("MIDORI_single_species_input_for_PHAT_algo.fasta", "w+")

uniq_taxonomies = []
double_taxonomies = set()

checking_var = 0

for line in input:
	if line[0] == ">" :

		checking_var = 1
		taxon = ''
		elements = line.split("\t")
		taxonomy= elements[1]

		if taxonomy not in uniq_taxonomies:
			uniq_taxonomies.append(taxonomy)
			output.write(line)
		else:
			checking_var = 0
			double_taxonomies.add(taxonomy)

	else:
		if checking_var == 1:
			output.write(line)
		else:
			continue

