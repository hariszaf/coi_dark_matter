# Python script to get only the sequences for which we have a full taxonomy
# Use the one line sequnence file


initial_sequence_file = open("ncbi_ids_and_seq.tsv", "r")
taxonomies_file = open("ids_and_semicolomns_taxonomies", "r")
complete_sequence_file = open("bold_bacteria_full_taxonomy_seq.fasta", "w+")


dict_with_sequenses_and_ids = {}
for line in initial_sequence_file:

    entry_elements = []
    line = line.split("\t")
    dict_with_sequenses_and_ids[line[0]] = line[2]


for line in taxonomies_file:

    line = line.split("\t")
    seq_id = line[0]
    taxonomy = line[1]

    if seq_id in dict_with_sequenses_and_ids.keys():

        complete_sequence_file.write(">" + seq_id + "\t" + taxonomy + dict_with_sequenses_and_ids[seq_id])
