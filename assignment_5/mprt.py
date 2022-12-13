from Bio import SeqIO
from Bio.SeqRecord import SeqRecord
import re
from urllib.request import urlopen

with open("rosalind_mprt.txt") as h:
    ID_list = []
    for line in h.readlines():
        ID_list.append(line.strip())

print(ID_list)



for ID in ID_list:
    response = urlopen(f"http://www.uniprot.org/uniprot/{ID}.fasta")
    fasta = response.read().decode("utf-8", "ignore").splitlines()
    seq = ''.join(fasta[1:])
    match = re.finditer(r"N[^P][ST][^P]", seq)
    if match:
        print(ID)
        print(*[m.start()+1 for m in match])