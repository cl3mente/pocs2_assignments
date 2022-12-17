from Bio import SeqIO
from Bio import Seq
import Bio
import re
import sys

def possible_prot(seq):

    # positions of the start codon, "AUG", given by regex matches
    start = [m.start() for m in re.finditer("AUG", seq)]
    # print(start)

    candidate = []

    for i in start:
        codons = []
        subseq = seq[i:]
        # print(subseq)
        for j in range(0,len(subseq),3):
            codons.append(subseq[j:j+3])
        # print(codons)
        for c in range(len(codons)):
            if codons[c] in ["UGA", "UAG", "UAA"]:
                codons = codons[:c]
                cand = "".join(codons)
                candidate.append(Bio.Seq.Seq(cand).translate())
                break
        # print(cand)
        
    return candidate

with open("rosalind_orf.txt") as f:
    input_record = SeqIO.read(f,'fasta')

seq1 = str(input_record.seq.transcribe())
seq2 = str(input_record.seq.reverse_complement().transcribe())

# print(seq1)
# print(seq2)

prot1 = possible_prot(seq1)
prot1 += possible_prot(seq2)
prot1 = set(prot1)

with open("answer.txt", "x") as f:
    sys.stdout = f
    for i in prot1:
        print(i)