#!/usr/bin/python3

# script name: get_dna_seq.py
# developed by: Haris Zafeiropoulos
# date: 2021.07.24
# framework: darn project
# usage: ./get_dna_seq.py  > SEQ_DNA.fasta


import sys, time
import subprocess

coordinates_file   = open('final_coordinates.tsv', 'r')
log_file           = open('downloads.log', 'w+')

for entry in coordinates_file: 

   genome_id       = entry.split(":")[0]
   seq_coordinates = entry.split(":")[1]
   start           = seq_coordinates.split("..")[0]
   end             = seq_coordinates.split("..")[1]
   log_file.write(entry)
   subprocess.run(["/home1/haris/programs/edirect/efetch", "-db", "nuccore", "-id", genome_id, "-seq_start", start, "-seq_stop", end, "-format", "fasta" ])

   time.sleep(0.4)

