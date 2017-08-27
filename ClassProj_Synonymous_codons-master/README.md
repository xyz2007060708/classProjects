Synonymous_codons
=================
Synonymous  codons  are  distinct  3-nucleotide  codons  that  code  for  the  same  amino  acid.  While 
synonymous  codons  are  used  interchangeably,  they  are  not  used  equally  frequently  within  coding 
regions of the genome.  In this exercise you will write a Python program to analyze the codon usage in 
the human genome based on a sampling of RNA transcript sequences.  Each transcript sequence will be provided to you in a file following FASTA format.  The nucleotide position in the file of the start codon is 
provided as well.  Your program should accept one or more file name and start position pairs.  The 
output of the program should be a list of the 20 amino acids and "Stp"  (sorted in alphabetic order by 
three letter name).  For each amino acid list the synonymous codons, and the number of times it was 
seen within the supplied coding sequences, and the percent utilization of this codon among all its 
synonymous codons.  These percentages should sum to 100% for each amino acid. 
Your  program  should  examine  the  following  four  mRNA  transcripts  (with  start  codon  offset  in 
parentheses): insulin (60), hemoglobinB (51), rhodopsin (96), and collagen1 (127).  Your program should 
print the aggregated results when run as follows: 
python hw2.py insulin.fa 60 hemoglobinB.fa 51 rhodopsin.fa 96 collagen1.fa 127 