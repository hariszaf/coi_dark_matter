#!/usr/bin/python3

import requests
import os, time, sys

# As you can see, in the end of the query there is a value for the WebEnv parameter; 
# this needs to change accordingly with the output of the previous piece of code
# You need to check the response_file.xml to get the WebEnv value returned and add it to the url query
webenv = "MCID_60f8643eb8e3924052041fe1"
count = 487629
key = 1


url_prefix = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?"
url_suffix = "&rettype=fasta"

db = "db=protein"
key = "query_key=1"
web_env = "WebEnv=" + webenv
retmax = 50
paging = "retmax=" + str(retmax)

path = os.getcwd()
filename = path + "/bacteria_protein_coi_sequences.fasta"

if not os.path.exists(filename):
    open(filename, 'w').close()



restart = 426700
while restart < count: 

   restart += retmax
   current_count = "retstart=" + str(restart)


   efetch_url = url_prefix + "&" + db + "&" + web_env + "&" + key + "&" + current_count + "&" + paging + url_suffix

   print(efetch_url)
   print(restart)
   seqs = requests.get(efetch_url)

   # Write down seqs get in a file
   h = open("bacteria_protein_coi_sequences.fasta","a+")
   h.write(seqs.text)
   h.close()

   time.sleep(0.2)


   



