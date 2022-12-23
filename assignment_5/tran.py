from Bio import SeqIO
with open("rosalind_tran.txt") as h:
    s1, s2 = SeqIO.parse(h, 'fasta')
    s1,s2 = s1.seq, s2.seq

print(s1,s2, sep="\n")

transitions = [("A","G"), ("G","A"), ("C","T"), ("T","C")]
transversions = [("A","T"), ("A", "C"), ("G", "C"), ("G", "T"), ("T", "A"), ("T", "G"), ("C", "A"), ("C", "G")]

transition_count = 0
transversion_count = 0
for i in range(len(s1)):
    if (s1[i], s2[i]) in transitions:
        transition_count += 1
    if (s1[i], s2[i]) in transversions:
        transversion_count += 1

print(transition_count/transversion_count)

