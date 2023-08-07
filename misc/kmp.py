from Bio import SeqIO

with open("rosalind_kmp.txt") as h:
    s = str(SeqIO.read(h, 'fasta').seq)

arr = 