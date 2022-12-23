from Bio import SeqIO

with open("rosalind_long.txt") as h:
    reads = []
    for read in SeqIO.parse(h, "fasta"):
        reads.append(str(read.seq))

result = ""

print(*reads, sep="\n")

def superstring(reads):
    #this function takes a list and returns a list with pairwise superstrings (?)
    match = []

    if len(reads) == 1:
        return reads
        #termination condition
    else:
        for i in reads:
            for j in reads:
                if i != j:
                    
                    #matching the start of a string i with the end of a string j

                    k = len(i)//2
                    scan = i[:k]

                    while scan in j and k <= len(i):
                        k += 1
                        scan = i[:k]
                    match.append(j + i[k:])

                    #matching the end of a string with the start of a string

                    k = len(i)//2
                    scan = i[k:]

                    while scan in j and k >= 0:
                        k -= 1
                        scan = i[k:]
                    match.append(i[:k] + j)
        return superstring(match)


print(superstring(reads))
