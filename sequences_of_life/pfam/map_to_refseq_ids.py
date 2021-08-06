#!/usr/bin/python3

# script name: map_to_refseq_ids.py
# developed by: Haris Zafeiropoulos
# date: 2021.07
# framework: darn project 
# usage: ./map_to_refseq_ids.py 

import sys, re, time
import requests


seq_file = open('uniprot_ids.tsv', 'r')
query = ''
counter = 1

uniprot_url = 'https://www.uniprot.org/uniprot/'


f = open('mappings_from_pfam_to_uniref.tsv', 'a')
for acc_id in seq_file:

   print(acc_id)

   acc_id = acc_id[:-1]
   url_to_source = uniprot_url + acc_id + '.xml'
   
   get_data = requests.get(url_to_source)
   get_data = get_data.text
   get_data = get_data.split("\n")

   genome_id = ''

   for term in get_data:

      if 'dbReference type="EMBL"' in term :

         if genome_id == '':

            genome_id = term 


      if 'protein sequence ID' in term: 

         protein_id_in_genome = term


   gid = genome_id[29:-3]
   pid = protein_id_in_genome[44:-3]

   f.write(acc_id + "\t" + gid + "\t" + pid + "\n")

   time.sleep(0.4)

