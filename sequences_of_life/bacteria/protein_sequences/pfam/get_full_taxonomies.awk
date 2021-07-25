#!/usr/bin/gawk -f

# script name: get_full_taxonomies.awk
# developed by: Haris Zafeiropoulos
# date: 2021.07.24
# framework: darn project
# usage: ./get_full_taxonomies.awk coordinates/xaa /home1/haris/Desktop/ncbi_taxonomy_dump/nucl_gb.accession2taxid


(ARGIND==1){

   gb_accession[$1]=$1

}


(ARGIND==2){

    FS="\t"

    if ($1 in gb_accession) {
#        print("got a match")
        gb_accession_ncbi_id[$1]=$3
    }
}

(ARGIND==3){

   if ($1 in gb_accession_ncbi_id){
      print($1 "\t" gb_accession_ncbi_id[$1]) 
   }

}


