#!/bin/bash

IFS=$'\n'; for p in $(cat protein_ids.tsv);
do

   /home/haris/edirect/esearch -db protein -query $p | /home/haris/edirect/efetch -format gp > tmp.txt

   if grep -q "coded_by=" tmp.txt; then

      echo -n $p "   " >> test
      grep "coded_by=" tmp.txt  >> test 
      sleep 0.5s

      rm tmp.txt

   else
      echo $p "was not retrieved" >> no_coordinates_found.tsv

   fi
   echo $p
   echo '------'

done

sed 's/  */\t/g'  test > cordinates.tsv 
