#!/bin/bash

for filename in ids/*; do

   [ -e "$filename" ] || continue
   echo $filename
   echo "*******************************"

   IFS=$'\n'; for p in $(cat $filename);
   do

      /home/haris/edirect/esearch -db protein -query $p | /home/haris/edirect/efetch -format gp > tmp.txt

      if grep -q "coded_by=" tmp.txt; then

         echo -n $p "   " >> coordinates_spaces.tsv
         grep "coded_by=" tmp.txt  >> coordinates_spaces.tsv
         sleep 0.5s

         rm tmp.txt

      else
         echo $p "was not retrieved" >> no_coordinates_found.tsv

      fi
      echo $p
      echo '------'

   done
done

sed 's/  */\t/g'  no_coordinates_found.tsv > cordinates.tsv 