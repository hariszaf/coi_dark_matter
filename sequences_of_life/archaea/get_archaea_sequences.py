#!/usr/bin/python3.5

import requests
import re

db = "nucleotide"
query = "coxi[all fields] or coi[all fields] or cytochrome c oxidase subunit i[all fields] or co1 AND (archaea[filter] AND (1[SLEN]:2000[SLEN])) "


#assemble the esearch URL
base = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/"

url = base + "esearch.fcgi?db=" + db + "&term=" + query + "&usehistory=y"
response = requests.get(url)

f = open("response_file.xml","w+")
f.write(response.text)
f.close()

# After the response_file.xml is done, we get the code from WebEnv key, we replace the one in here and run the following part of the script 
seqs=requests.get("https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=nucleotide&query_key=1&WebEnv=NCID_1_177652469_130.14.22.76_9001_1561390561_1117843173_0MetA0_S_MegaStore&rettype=fasta")

h = open("sequences.fasta","w+")
h.write(seqs.text)
h.close()
