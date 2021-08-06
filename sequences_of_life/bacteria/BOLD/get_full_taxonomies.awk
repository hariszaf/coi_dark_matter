#!/usr/bin/gawk -f

# script name: get_full_taxonomies.awk
# developed by: Haris Zafeiropoulos
# date: 2021.07.24
# framework: darn project : map ncbi ids from BOLD sequences to their complete taxonomies
# usage: ./get_full_taxonomies.awk temp.taxonomy ncbi_ids_and_seq.tsv > ncbi_id_compl_tax_singleline.fasta


(ARGIND==1){

   FS=" "
   ncbi_id_full_taxonomy[$1]=$2

}


(ARGIND==2){

    FS="\t"
    if ($1 in ncbi_id_full_taxonomy) {
        print(">" $1 "\t"  ncbi_id_full_taxonomy[$1])
        print($3)

    }
}



