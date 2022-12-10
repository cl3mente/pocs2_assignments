import Bio.SeqIO
import re

with open("rosalind_lcsm.txt") as h:
    seqlist = [str(seq.seq) for seq in Bio.SeqIO.parse(h, "fasta")]

# print(seqlist)

consensus = ""
scan = ""
resultList = []

for i in range(len(seqlist[0])):
    scan += seqlist[0][i]
    check = True
    for seq in seqlist:
        if scan not in seq:
            scan = ""
            check = False
            resultList.append(consensus)
            continue
    if check == True:
        consensus = scan

print(resultList)
print(max(resultList, key=len))
