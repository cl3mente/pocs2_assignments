from Bio import SeqIO
import sys

with open("rosalind_long.txt") as h:
    reads = []
    for read in SeqIO.parse(h, "fasta"):
        reads.append(str(read.seq))

def superstring(reads):
    #this function takes a list and returns a superstring

    match = reads.pop(0)
    index = 0

    while reads != []:

        i = reads[index]
        k = len(i)//2

        #matching the start of a string i with the end of a string j

        scan = i[:k]

        if scan in match:
            match = match[:match.index(scan)] + i
            reads.remove(i)
            index = 0
            continue
        

        #matching the end of a string with the start of a string

        scan = i[k:]

        if scan in match:
            match = i + match[match.index(scan) + len(scan):]
            reads.remove(i)
            index = 0
            continue
        else:        
            #increment
            index += 1
    
    return match

with open("answer.txt", "x") as h:
    sys.stdout = h
    print(superstring(reads))


# risultato = ATTAGACCTGCCGGAATAC
# my result = ATTAGACCTGCCGGAATAC