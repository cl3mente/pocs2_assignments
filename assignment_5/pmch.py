from Bio import SeqIO
import sys

with open("rosalind_pmch.txt") as h:
    seq = SeqIO.read(h, "fasta").seq

def pmch(n):
    if n == 1:
        result = 1
    else:
        result = (n) * pmch(n-1)
    return result

print(seq)

nA = seq.count("A")
nC = seq.count("C")

result = pmch(nA) * pmch(nC)

print(result)
