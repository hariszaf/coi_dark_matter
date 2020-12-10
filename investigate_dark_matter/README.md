In this directory we version the scripts needed to place our query sequences on the magic tree we built. 

A number of fasta files will be saved on this path on Zorba; however they will not be displayed here 
as their size does not allow this. 



# to convert multi line fasta to single line
awk '{if(NR==1) {print $0} else {if($0 ~ /^>/) {print "\n"$0} else {printf $0}}}' interleaved.fasta > singleline.fasta




# to convert single line fasta to multi line
fold -w 80 marine_query_short_dark_matter_top6.fasta > marine_query_short_dark_matter_top6_multilne.fasta


# to relabel the Otus on the multiline fasta
awk -v n=1 '{if($x~/>/){sub(/>.*/, ">Otu" n); print; n++}else{print $0}}' marine_query_short_dark_matter_top6_multilne.fasta > marine_query_short_dark_matter_top6_multilne_labeled.fasta

