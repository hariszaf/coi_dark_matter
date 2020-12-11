#!/usr/bin/python3.5

phyla = [    
    "Acanthocephala",
    "Annelida",
    "Apicomplexa",
    "Arthropoda",
    "Ascomycota",
    "Bacillariophyta",
    "Basidiomycota",
    "Blastocladiomycota",
    "Brachiopoda",
    "Bryozoa",
    "Cercozoa",
    "Chaetognatha",
    "Chlorophyta",
    "Chordata",
    "Chytridiomycota",
    "Ciliophora",
    "Cnidaria",
    "Cryptomycota",
    "Ctenophora",
    "Cycliophora",
    "Dicyemida",
    "Discosea",
    "Echinodermata",
    "Endomyxa",
    "Entoprocta",
    "Euglenozoa",
    "Evosea",
    "Gastrotricha",
    "Gnathostomulida",
    "Haptista",
    "Hemichordata",
    "Heterolobosea",
    "Imbricatea",
    "Kinorhyncha",
    "Mollusca",
    "Mucoromycota",
    "Nematoda",
    "Nematomorpha",
    "Nemertea",
    "Onychophora",
    "Perkinsozoa",
    "Phoronida",
    "Placozoa",
    "Platyhelminthes",
    "Porifera",
    "Priapulida",
    "Rhodophyta",
    "Rotifera",
    "Streptophyta",
    "Tardigrada",
    "Tubulinea",
    "Xenacoelomorpha",
    "Zoopagomycota",
]



file = open("consensus_sequences_min_tax_level_4.fasta", "r")

counts = {}

for line in file:
    if line[0] != ">" :
        continue
    else:
        
        for phylum in phyla:
            
            if phylum in line:
                
                if phylum not in counts.keys():
                    
                    counts[phylum] = 1
                else:
                    counts[phylum] += 1
                    

print(counts)                
sum = 0
for value in counts.values():
    sum += value
print(sum)





