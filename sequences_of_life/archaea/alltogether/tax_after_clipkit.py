#!/usr/bin/python3
import os
import sys
path = os.getcwd()

init_aln        = open(path + '/aligned_archaea.aln', 'r')
trimmed_aln       = open(path + '/trimmed_archaea.aln', 'r')
fixed_trimmed_aln = open(path + '/fixed_tax_trimmed_archaea.aln', 'w')


taxonomies_list = []
for line in init_aln: 
   if line[0] == ">" :
     
      gid      = line.split("\t")[0]
      taxonomy = line.split("\t")[1]
      taxonomy = taxonomy.replace(' ', ':')
      entry    = (gid, taxonomy)

      taxonomies_list.append(entry)


counter = 0
for line in trimmed_aln:

   if line[0] == ">" :

      fixed_trimmed_aln.write(line[:-1] + " " + taxonomies_list[counter][1])
      counter += 1


   else: 

      fixed_trimmed_aln.write(line)


