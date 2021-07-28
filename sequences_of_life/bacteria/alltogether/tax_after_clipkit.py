#!/usr/bin/python3
import os
import sys
path = os.getcwd()

init_aln        = open(path + '/cheat_taxonomies', 'r')
trimmed_aln       = open(path + '/bacteria_alignment_trimmed.aln', 'r')
fixed_trimmed_aln = open(path + '/fixed_tax_trimmed_bacteria.aln', 'w')


taxonomies_list = []
for line in init_aln:
   if line[0] == ">" :

      gid      = line.split("\t")[0]
      taxonomy = line.split("\t")[1:]
      taxonomy = ''.join(taxonomy)
      taxonomy = taxonomy.replace(' ', ':')
      entry    = (gid, taxonomy)

      taxonomies_list.append(entry)



counter = 0
for line in trimmed_aln:

   if line[0] == ">" :

      fixed_trimmed_aln.write(line[:-1] + " " + taxonomies_list[counter][1] + "\n")
      counter += 1


   else:

      fixed_trimmed_aln.write(line)


