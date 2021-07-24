#!/usr/bin/python3

import re, os

path = os.getcwd()
directory = path + "/bold_xml_files/"
output_file = open("ncbi_ids_and_seq.tsv", "w+")

check = False

ncbi_id = ""
sequence = ""


taxa_ids = set()

for file in os.listdir(directory):

	print(file)
	phylum = file[:-4]
	file = directory + file
	file = open(file, "r")

	for line in file:

		if "</record>" in line: 
			ncbi_id = ""
			sequence = ""

		line.encode('ascii','ignore').decode('UTF-8','ignore')

		if "extrainfo" in line: 

			try:
				ncbi_id = line.split(":")[1]
				ncbi_id = ncbi_id[:-13]

			except:
				ncbi_id = ""

		if "nucleotides" in line:

			try:

				sequence = line.split(">")[1]
				sequence = sequence.split("<")[0]

			except:
				sequence = ""

		if  ncbi_id != "" and sequence != "" :

			if ncbi_id not in taxa_ids:

				output_file.write(ncbi_id + "\t" + phylum + "\t" + sequence + "\n")
				taxa_ids.add(ncbi_id)
				ncbi_id = ""
				sequence = ""

	file.close()
