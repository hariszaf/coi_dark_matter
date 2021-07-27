#!/usr/bin/gawk -f

(ARGIND==1){

   FS="\t"
   seq_ncbi_id[$3]=$1
   seq_taxonomy[$3]=$2

}

END {


   for (seq in seq_ncbi_id) {

      print(">" seq_ncbi_id[seq] "\t" seq_taxonomy[seq])
      print(seq)

   }


}