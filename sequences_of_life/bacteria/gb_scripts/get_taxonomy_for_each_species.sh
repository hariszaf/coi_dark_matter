#!/bin/bash


#input="/home1/haris/Desktop/jens/bacteria/only_best.txt"
input="/home1/haris/Desktop/stsm/sequences_of_life/bacteria"



#	/home1/haris/edirect/esearch -db taxonomy -query "$line[Scientific Name]" | /home1/haris/edirect/efetch -format xml | /home1/haris/edirect/xtract -pattern Lineage -element Lineage -tab "\n" >> apapapa.txt





#IFS=$'\n' read -d '' -r -a lines < /home1/haris/Desktop/jens/bacteria/only_best.txt
IFS=$'\n' read -d '' -r -a lines < $input/only_best.txt




for line in "${lines[@]}"
do
   :
   echo $line

#   /home1/haris/edirect/esearch -db taxonomy -query "$line[Scientific Name]" | /home1/haris/edirect/efetch -format xml | /home1/haris/edirect/xtract -pattern Lineage -element Lineage -tab "\n" >> apapapa.txt
   /home1/haris/programs/edirect/esearch -db taxonomy -query "$line[Scientific Name]" | /home1/haris/programs/edirect/efetch -format xml | /home1/haris/programs/edirect/xtract -pattern Lineage -element Lineage -tab "\n" >> apapapa.txt

   sleep 10


done
