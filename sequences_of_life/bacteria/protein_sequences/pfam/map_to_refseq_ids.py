#!/usr/bin/python3
import sys, re, time
import requests
import urllib


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











   # counter += 1

   # if float(counter)%100 == 1: 

   #    print(query)

   #    # use API to get the ids
   #    params = {
   #       'from'  : 'ACC+ID',
   #       'to'    : 'P_ENTREZGENEID',
   #       'format': 'tab',
   #       'query' : query
   #    }

   #    data = urllib.parse.urlencode(params)
   #    data = data.encode('utf-8')
   #    req = urllib.request.Request(url, data)

   #    with urllib.request.urlopen(req) as f:
   #       response = f.read()
      
   #    g1 = open('refseq_nt.tsv', 'w')
   #    g1.write(response1.decode('utf-8'))

   #    # re-initiate counting and query back 
   #    counter = 1
   #    query = ''

   #    sys.exit(0)

   # else: 
   #    query += acc_id[:-1] + " "








