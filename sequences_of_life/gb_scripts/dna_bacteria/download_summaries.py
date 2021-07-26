#!/usr/bin/python3.5

import requests
import re


# You need to check the response_file.xml to get the WebEnv value returned and add it to the url query. As we did for the download_sequences.py
webenv = "MCID_5f45715d8e3d0d1989309a0d"
url_prefix = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esummary.fcgi?db=nucleotide&query_key=1&WebEnv="
url_suffix = "&version=2.0"
url = url_prefix + webenv + url_suffix

# Get the url 
metadata = requests.get(url)

# Create a file and keep the sequences retrieved
h = open("bacteria_summaries.xml","w+")
h.write(metadata.text)
h.close()

