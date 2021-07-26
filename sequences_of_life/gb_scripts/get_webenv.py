#!/usr/bin/python3.5

import requests
import re

db = "nucleotide"
query = "Coi[All Fields] OR Cytochrome c oxidase subunit I[All+Fields] OR CO1[All Fields] AND (Bacteria[Organism] OR Bacteria Latreille+et+al. 1825[Organism]) AND (1[SLEN]:2000[SLEN])) AND (bacteria[filter])"


#assemble the esearch URL
base = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/"

url = base + "esearch.fcgi?db=" + db + "&term=" + query + "&usehistory=y"


response = requests.get(url)

f = open("response_file.xml","w+")
f.write(response.text)
f.close()























#seqs=requests.get("https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=nucleotide&query_key=1&WebEnv=NCID_1_177179919_130.14.22.76_9001_1561386447_363981351_0MetA0_S_MegaStore&rettype=fasta")
#h = open("response_file.xml","w+")
#h.write(seqs.text)
#h.close()
