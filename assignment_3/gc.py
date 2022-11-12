from Bio import SeqIO

seq = SeqIO.parse("rosalind_gc.txt", "fasta")


max = 0
for s in seq:
    ID = s.id
    content = s.seq
    gcscore = ((content.count("G")+content.count("C"))/len(content))*100
    if gcscore > max:
        max = gcscore
        maxID = ID

print(maxID, max)
