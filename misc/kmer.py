from Bio import SeqIO

with open("rosalind_kmer.txt") as h:
    s = str(SeqIO.read(h, "fasta").seq)

    

def kmer(s, k):
    kmer = {}
    for i in range(len(s) - k + 1):
        if s[i:i+k] not in kmer:
            kmer[s[i:i+k]] = 0
        kmer[s[i:i+k]] += 1

    ks = sorted(kmer.keys())
    kmer = {k:v for k,v in zip(ks, [kmer[k] for k in ks])}        

    result = list(kmer.values())
    print(*result, sep = " ")


        

kmer(s, 4)