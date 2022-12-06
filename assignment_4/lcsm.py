import Bio.SeqIO
with open("rosalind_lcsm.txt") as h:
    seqlist = [str(seq.seq) for seq in Bio.SeqIO.parse(h, "fasta")]

print(seqlist)

result = ""

for base in seqlist[0]:
    check = "true"
    for i in range(1, len(seqlist)):
        if base not in seqlist[i]:
            check = "false"
        if check == "true":
            result += base