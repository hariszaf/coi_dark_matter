#!/usr/bin/python3

# Bacteria
import requests
import re

db = "protein"

# In the following query we describe what sequences we need to get. Filters allow to get exactly what we need from the NCBI database
query = "(((cytochrome c oxidase subunit I) OR cbb3-type cytochrome c oxidase subunit I) AND Bacteria[Organism]) AND 50:350[Sequence Length] "

# Get the WebEnv code - this is different every time you run this; thus we keep in a text file and then feed it accordingly in a next command
base = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/"
url = base + "esearch.fcgi?db=" + db + "&term=" + query + "&usehistory=y"
response = requests.get(url)

print(response.text)
