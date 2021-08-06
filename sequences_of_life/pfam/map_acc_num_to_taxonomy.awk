#!/usr/bin/gawk -f

# script name: build_seq_file.awk
# developed by: Haris Zafeiropoulos
# date: 2021.07.24
# framework: darn project
# usage: ./map_acc_num_to_taxonomy.awk PAIRS /home1/haris/Desktop/ncbi_taxonomy_dump/fullnamelineage.dmp  > IDS_TAXA


(ARGIND==1){

  FS="\t"
  ncbi_id_accession[$2][$1]= $1

}

(ARGIND==2){

   FS="|"

   pattern = substr($1, 1, length($1)-1)


   if (pattern in ncbi_id_accession ){

      for (i in ncbi_id_accession[pattern]) {

         print ncbi_id_accession[pattern][i] "\t" pattern "\t" $3 " " $2

      }
   }
}

