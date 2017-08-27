#python hw2.py insulin.fa 60 hemoglobinB.fa 51 rhodopsin.fa 96 collagen1.fa 127 
import sys

files = sys.argv[1::2]
start = [int(i)-1 for i in sys.argv[2::2]]
codon = {'GCT':'Ala', 'GCC':'Ala', 'GCA':'Ala', 'GCG':'Ala', 
         'TTA':'Leu', 'TTG':'Leu', 'CTT':'Leu', 'CTC':'Leu', 'CTA':'Leu', 'CTG':'Leu', 
         'CGT':'Arg', 'CGC':'Arg', 'CGA':'Arg', 'CGG':'Arg', 'AGA':'Arg', 'AGG':'Arg', 
         'AAA':'Lys', 'AAG':'Lys', 
         'AAT':'Asn', 'AAC':'Asn',
         'ATG':'Met',
         'GAT':'Asp', 'GAC':'Asp',
         'TTT':'Phe', 'TTC':'Phe',
         'TGT':'Cys', 'TGC':'Cys',
         'CCT':'Pro', 'CCC':'Pro', 'CCA':'Pro', 'CCG':'Pro',
         'CAA':'Gln', 'CAG':'Gln',
         'TCT':'Ser', 'TCC':'Ser', 'TCA':'Ser', 'TCG':'Ser', 'AGT':'Ser', 'AGC':'Ser',
         'GAA':'Glu', 'GAG':'Glu',
         'ACT':'Thr', 'ACC':'Thr', 'ACA':'Thr', 'ACG':'Thr',
         'GGT':'Gly', 'GGC':'Gly', 'GGA':'Gly', 'GGG':'Gly',
         'TGG':'Trp',
         'CAT':'His', 'CAC':'His',
         'TAT':'Tyr', 'TAC':'Tyr',
         'ATT':'Ile', 'ATC':'Ile', 'ATA':'Ile',
         'GTT':'Val', 'GTC':'Val', 'GTA':'Val', 'GTG':'Val',
         'TAA':'Stp', 'TGA':'Stp', 'TAG':'Stp'
         }

#read sequence data
seq = []
for x in files:
    f = open(x, 'r')
    f.readline() #skip the first line
    lines = ''
    for y in f:
        lines += y.strip()
    seq.append(lines)
    f.close()

#Count codon numbers
count = {key:0 for key in codon}    #construct counting map
for i in xrange(len(seq)):  #for each input sequence
    curr = seq[i]
    pos = start[i]
    while pos+3 < len(curr):
        curr_codon = curr[pos:pos+3]
        count[curr_codon] += 1
        if curr_codon == 'TAA' or curr_codon == 'TGA' or curr_codon == 'TAG':
            break
        else:
            pos += 3

#construct result map (use amino acids as keys )
res = {}
for (key,value) in codon.items():
    if res.get(value) == None:
        res[value] = {key : count[key]}
    else:
        res[value][key] = count[key]
  
#calculate percentage
for (key,value) in res.items():
    sum_num = sum(value.values())
    for (k,v) in value.items():
        value[k] = [v, '%i%%' %round(v*100.0/sum_num)] #real number and percentage as elements

#save result in a text file with amino acid name sorted
f = open('result.txt','w')
for x in sorted(res):
    f.write('%s\t%s\n' %(x,res[x]))
f.close()

if __name__ == '__main__':
    print files
    print start
    for x in res.items():
        print x
    