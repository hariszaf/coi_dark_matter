#!/usr/bin/python3.5

bacteria_path = "/home1/haris/Desktop/stsm/sequences_of_life/bacteria"
sequences_file = bacteria_path + "/bacteria_sequences.fasta"
caption_taxid_taxonomy_file = bacteria_path + "/caption_taxid_taxonomy.tsv"
output_file = bacteria_path + "/bacteria_sequences_taxonomy.fasta"
banned_captions = bacteria_path + "/non_coi_captions.tsv"

# Open the file with the sequences retrieved
with open(sequences_file, 'r') as seq_file:
    
    # And the 3 - column file
    with open(caption_taxid_taxonomy_file, 'r') as tax_file:
 
        # Build a dictionary with caption : taxonomy pairs    
        caption_taxonomy = {}
        for line in tax_file:
            line = line.split("\t")
            caption = line[0]
            taxonomy = line[2]            
            caption_taxonomy[caption] = taxonomy

        tax_file.close()

        # Open the output file 
        with open(output_file, "w+") as output:

            # And the file with the non COI sequences' captions; keep those in a list  
            with open(banned_captions, "r") as banned:
                banned_captions = []
                for entry in banned:
                    banned_captions.append(entry[:-1])
                banned.close()
                
            # Parse the sequence file to match
            checking_var = 1
            for line in seq_file:
                
                if line[0] == ">" :
                    
                    checking_var = 1
                    line = line.split(" ")
                    caption = line[0][1:-2]
                    
                    # Check if the caption of the study is among the banned ones
                    if caption not in banned_captions:

                        new_line = ">" + caption + " " + caption_taxonomy[caption]
                        output.write(new_line)

                    # If it is change the checking_var to 0; this will allow us not to print the sequence lines of this entry to the new file. 
                    else:
                        checking_var = 0

                else:
                    
                    if checking_var == 1:
                        output.write(line)
                    else:
                        continue
seq_file.close()
output.close()
