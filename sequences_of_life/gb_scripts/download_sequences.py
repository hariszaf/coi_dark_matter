#!/usr/bin/python3.5

import requests
import re


# You need to check the response_file.xml to get the WebEnv value returned and add it to the url query

webenv = "MCID_5f45715d8e3d0d1989309a0d"
url_prefix = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=nucleotide&query_key=1&WebEnv="
url_suffix = "&rettype=fasta"
url = url_prefix + webenv + url_suffix

# Get the url 
seqs = requests.get(url)

# Create a file and keep the sequences retrieved
h = open("bacteria_sequences.fasta","w+")
h.write(seqs.text)
h.close()

