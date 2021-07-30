#!/usr/bin/python3

import sys
import os, re

path                    = os.getcwd()
mytaxonomy              = open('curated_taxonomies_format')
my_alignment_taxonomies = open('taxonomies_present.tsv')
my_alignment            = open('trimmed_aligned_bascteria.aln')


taxonomy = {}
for line in mytaxonomy: 

   line = line.split("\t")
   line = list(filter(None, line))
   line = line[:-1]

   last_element = line[-1]

   if last_element.isdecimal():

      query = line[-2] + ":" + last_element
      line = line[:-1] 
      line.append(":" + last_element)

   else:

      query = last_element

   new_taxonomy = ';'.join(line)
   new_taxonomy = new_taxonomy.replace(";:", ":")

   taxonomy[query] = new_taxonomy


counter = 0
final_taxonomy = {}
for line in my_alignment:

   if line[0] == ">":

      current_taxonomy = ''

      pattern = "unclassified_Bacteria"

      if pattern not in line: 

         line = line.split(' ')
         if len(line) == 2:
            query = line[1].split(';')[-1]

            if query[:-1] in taxonomy.keys():

               current_taxonomy = taxonomy[query[:-1]]
               
            # else: 

            #    if "aceae" in line[1]:
                  
            #       taxa = line[1].split(";")
            #       for taxon in taxa: 
            #          if "aceae" in taxon:
            #             index = taxa.index(taxon)

            #       if index > 4:
            #          current_taxonomy = ';'.join(taxa[:5]) + ";" + taxa[index] + ';' + ';'.join(taxa[index + 1:])

            #       else: 

            #          gap  = 6 - index
            #          fill = gap*(";" + taxa[index])
            #          current_taxonomy = ';'.join(taxa[:index]) + fill + ";" + ';'.join(taxa[index + 1:])
                     

         if len(line) == 3 : 

            query = line[1] + ":" + line[2]
            query = query.split(";")[-1]

            if query[:-1] in taxonomy.keys():

               current_taxonomy = taxonomy[query[:-1]]

            # else: 

            #    if "aceae" in line[1]:
                  
            #       taxa = line[1].split(";")
            #       for taxon in taxa: 
            #          if "aceae" in taxon:
            #             index = taxa.index(taxon)

            #       if index > 4:
            #          current_taxonomy = ';'.join(taxa[:5]) + ";" + taxa[index] + ';' + ';'.join(taxa[index + 1:])

            #       else: 

            #          gap  = 6 - index
            #          fill = gap*(";" + taxa[index])
            #          current_taxonomy = ';'.join(taxa[:index]) + fill + ";" + ';'.join(taxa[index + 1:])

      if current_taxonomy != '':
         print(line[0], "\t", current_taxonomy)


   elif current_taxonomy == '':
      continue

   else: 
      print(line)
                  