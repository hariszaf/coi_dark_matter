#!/usr/bin/gawk -f

# script name: build_seq_file.awk
# developed by: Haris Zafeiropoulos
# date: 2021.07.24
# framework: darn project
# usage: /build_seq_file.awk PAIRS /home1/haris/Desktop/ncbi_taxonomy_dump/fullnamelineage.dmp  > IDS_TAXA

(ARGIND==1){

   FS="\t"
   accession_ncbi_id[$1]=$2
   ncbi_id_accession[$2]=$1

}

(ARGIND==2){

   FS="|"

   $1 = substr($1, 1, length($1)-1)

   if ($1 in ncbi_id_accession){


      print ncbi_id_accession[$1] "\t" $1 "\t" $3 " " $2

   }

}


