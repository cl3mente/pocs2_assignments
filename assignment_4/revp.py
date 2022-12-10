from Bio import SeqIO
from Bio import SeqFeature

with open("rosalind_revp.txt") as f:
    for seq in SeqIO.parse(f, "fasta"):
        stretch = str(seq.seq)

substrings = {}
result = []

for i in range(len(stretch)):
    temp = []
    for j in range(i+4, len(stretch)+1):
        temp.append(stretch[i:j])
    substrings = dict.fromkeys(temp, i+1)

    for k in substrings:
        if len(k) in range(4,13) and k == SeqFeature.reverse_complement(k):
            result.append((substrings[k],len(k)))

for i in substrings:
    print(i, substrings[i])

result.sort()
for i in result:
    print(str(i[0]) + " " + str(i[1]))