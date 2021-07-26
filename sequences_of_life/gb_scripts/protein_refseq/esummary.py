#!/usr/bin/python3.5

import requests

# You need to check the response_file.xml to get the WebEnv value returned and add it to the url query. As we did for the download_sequences.py
webenv = "MCID_60f6075ad7dc1476bf3d02e3"

url_prefix = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esummary.fcgi?db=nucleotide&query_key=1&WebEnv="
url_suffix = "&version=2.0"
url = url_prefix + webenv + url_suffix

# Get the url
metadata = requests.get(url)

# Create a file and keep the sequences retrieved
h = open("bacteria_protein_summaries.fasta","w+")
h.write(metadata.text)
h.close()
