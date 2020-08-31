#!/usr/bin/python3.5

import sys

input = open("MIDORI_UNIQ_GB239_CO1_RDP_no_taxids.fasta","r")
#output = open("MIDORI_single_species_input_for_PHAT_algo.fasta", "w+")

# STEP 1
counter = 0
uniq_taxonomies = []
double_taxonomies = set()

checking_var = 0

for line in input:
	if line[0] == ">" :

		checking_var = 1

		counter += 1
		print(counter)
		taxon = ''
		line = line.split("\t")
		taxonomy= line[1]

		if taxonomy not in uniq_taxonomies:
			uniq_taxonomies.append(taxonomy)
		else:
			checking_var = 0
			double_taxonomies.add(taxonomy)

	else:
		if checking_var == 1:
                        output.write(line)
                    else:
                        continue






print(len(uniq_taxonomies))
sys.exit(0)

# STEP 2

checking_var = 0
#for line in input: 
#    if line[0] == ">":
    
















#with open(input, "r") as input:
#	records = []
#	current_record = []
#	for lineno, line in enumerate(input):
#
#		if lineno == 0:
#			current_record.append(line)
#
#		elif lineno % 2 == 0:
#			records.append(current_record)
#			current_record = []
#			current_record.append(line)
#		else:
#
#			current_record.append(line)
#
#print("the records found are: ")
#print(len(records))
#
#
#counter = 0 
#for record in records:
#	counter += 1 
#	print("i am looking to the record No:" + str(counter))
#	taxonomy = record[0].split(" ")
#	taxon= taxonomy[1:]
#	name = ''
#	for term in taxon[:-1]:
#		name += term + " "
#
#
#	if name in double_taxonomies:
#		print("I found a double")
#		double_taxonomies.remove(name)
#		continue
#	else:
#		for term in record:
#			output.write(term)
#
#
#
#
