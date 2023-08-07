from Bio import SeqIO
from Bio import Seq
import sys

with open('rosalind_corr.txt') as h:
    seqlist = [str(i.seq) for i in SeqIO.parse(h, 'fasta')]


def hamming(s1, s2):

    hamming = 0

    for i in range(len(s1)):
        if s1[i] != s2[i]:
            hamming += 1

    return hamming


correct = []
wrong = []

for s in seqlist:

    if (seqlist.count(s) + seqlist.count(Seq.reverse_complement(s))) >= 2:
        correct.append(s)

    else:
        wrong.append(s)


result = {}
for s in wrong:
    for c in correct:
        if hamming(s, c) == 1 and s not in result.keys():
            result.update({s: c})

        elif hamming(Seq.reverse_complement(s), c) == 1 and s not in result.keys():
            result.update({s: Seq.reverse_complement(c)})


sys.stdout = open('result.txt', 'x')

for i in result:
    print(i + '->' + result[i])
        
    
        

        



