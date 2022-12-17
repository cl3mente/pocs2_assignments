from Bio import SeqIO
import sys

with open("rosalind_grph.txt") as f:
    seqlist = [i for i in SeqIO.parse(f,'fasta')]   
    print([str(i.seq) for i in seqlist])

with open("answer.txt", "x") as f:
    sys.stdout = f

    result = []
    for seq1 in seqlist:
        for seq2 in seqlist:
            if seq2.seq[:3] == seq1.seq[-3:] and seq1.seq != seq2.seq:
                result.append((seq1.id,seq2.id))

    for i in result:
        print(*i)