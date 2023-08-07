from Bio import SeqIO
import itertools

with open("rosalind_pdst.txt") as h:
    seqs = [i.seq for i in list(SeqIO.parse(h, "fasta"))]


def pdist(s1, s2):
    
    hamming = 0

    for i in range(len(s1)):
        if s1[i] != s2[i]:
            hamming += 1

    return hamming / len(s1)


with open("result.txt", "x") as r:
    for s1 in seqs:
        for s2 in seqs:
            r.write("{:#.3g}".format(pdist(s1, s2)) + " ")
        r.write("\n")
