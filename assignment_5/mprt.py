from Bio import SeqIO
from Bio.SeqRecord import SeqRecord
import re
from urllib.request import urlopen
import sys

with open("rosalind_mprt.txt") as h:
    ID_list = []
    for line in h.readlines():
        ID_list.append(line.strip())

print(ID_list)

with open("answer.txt", 'x') as f:
    sys.stdout = f

    for preID in ID_list:
        ID = ""
        for i in preID:
            if i == "_":
                break
            ID += i
        
        response = urlopen(f"http://www.uniprot.org/uniprot/{ID}.fasta")
        fasta = response.read().decode("utf-8", "ignore").splitlines()
        seq = ''.join(fasta[1:])

        # use lookahead to find overlapping matches :(
        match = re.finditer("(?=(N[^P][ST][^P]))", seq)

        # create a list with all match positions
        mlist = [m.start()+1 for m in match]
        
        #if that list is empty, dont show it
        if mlist != []:
            print(preID)
            print(*mlist)