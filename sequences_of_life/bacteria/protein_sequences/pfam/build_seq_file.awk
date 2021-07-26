#!/usr/bin/gawk -f

# script name: get_full_taxonomies.awk
# developed by: Haris Zafeiropoulos
# date: 2021.07.24
# framework: darn project
# usage: ./build_seq_file.awk IDS_TAXA pfam_dna_sequences.fasta


(ARGIND==1){

   FS="\t"
   ncbi_id[$1]=$2 
   taxonomy[$1]=$4
}

(ARGIND==2){

   if (substr($0, 1, 1)!=">") {
      print($0)

   } else {

      id_tmp=gensub(/\..*/, "", "g", $0)
      id=gensub(/>/, "", "g", id_tmp)

      if (id in ncbi_id){
         print(">" ncbi_id[id] "\t" taxonomy[id] "\t" id )
      }

      else{
         print("not found" "\t" id)
      }

   }


}
