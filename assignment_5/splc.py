from Bio import SeqIO
from Bio.Seq import Seq
import re
import sys


with open("rosalind_splc.txt") as f:
    seqlist = [str(rec.seq) for rec in SeqIO.parse(f, "fasta")]
    main_Seq = seqlist.pop(0)

print(main_Seq)
print(seqlist)

for i in seqlist:
    pattern = i
    match = re.search(pattern, main_Seq)
    print(match)
    main_Seq = main_Seq[:match.start()] + main_Seq[match.start() + len(pattern):]


main_Seq = Seq(main_Seq)

with open("answer.txt", "x") as f:
    sys.stdout = f
    print(main_Seq.transcribe().translate()[:-1])
