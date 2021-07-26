#!/usr/bin/python3.5

import io

# Important note! 
# The fullnamelineage.dmp we are about to use is a non-ascii file; thus we need to remember forcing for the utf-8 encoding


# Files we need
parent_directory = "/home1/haris/Desktop/stsm/sequences_of_life/bacteria"
ncbi_taxonomy_fullname_file = parent_directory + "/ncbi_taxonomy/fullnamelineage.dmp"
caption_taxids_in_summaries_file = parent_directory + "/caption_taxid_in_summaries.tsv"


# Build a dictionary with the information included in the fullnamelineage.dmp file in a way that suits for our case

dict_ncbi_tax_id_full_taxonomy = {}

with io.open(ncbi_taxonomy_fullname_file, mode="r", encoding="utf-8") as tax_file:

    for entry in tax_file:


        elements = entry.split("\t")

        ncbi_tax_id = elements[0]
        species_name = elements[2]
        lineage = elements[4]

        # Process these elements to convert them in a format that suits to the needs of our study; see further on the text
        lineage = lineage.replace('cellular organisms; ','')
        lineage = lineage.replace('; ',';')
        lineage = lineage.replace(' ','_')

        species_name = species_name.replace(' ','_')

        # Build the full taxonomy of the species
        taxonomy = lineage + species_name
#        taxonomy = taxonomy.encode('utf-8')

        # Keep this info in the corresponding dictiontary
        dict_ncbi_tax_id_full_taxonomy[ncbi_tax_id] = taxonomy


print("-----------------------------------------------")

# Parse the file with both the caption and their corresponding TaxIds and add a column with the full taxonomy they match using the NCBI TaxId to do the matching
with open(caption_taxids_in_summaries_file) as f:

    our_taxa = {}

    for entry in f:

        elements = entry.split("\t")

        # As there is a new line character added in the ncbi id we have not to keep it
        entry_ncbi_id = elements[1][:-1]
        entry_caption = elements[0]
        our_taxa[entry_caption] = entry_ncbi_id


    # Parse the dictionary we built from the fullnamelineage.dmp file
    for ncbi_id, taxonomy in dict_ncbi_tax_id_full_taxonomy.items():

        # And check whether the ncbi id we have mathes with one from our taxa
        for caption, entry_ncbi_id in our_taxa.items():

            if ncbi_id == entry_ncbi_id:

                print("Got a match!")

                new_line = caption + "\t" + ncbi_id + "\t" + taxonomy + "\n"
                with open("caption_taxid_taxonomy.tsv", 'a+') as output:
                    output.write(new_line)
                    output.close()

