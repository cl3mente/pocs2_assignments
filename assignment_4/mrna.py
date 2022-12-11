with open("rosalind_mrna.txt") as f:
    prot = str(f.read().strip())


#build codon dictionary
with open("rna_codon_table.txt") as table:
    aa = []
    for line in table.readlines():
        line = line.strip()
        array = list(line.split(sep="      "))
        for i in array:
            pair = i.split()
            aa.append((pair[1]))

aa = [x for x in aa if x != "Stop"]
# print(aa)

codons = {}
for i in aa:
    codons.update(dict.fromkeys(i, aa.count(i)))

# print(codons)
    
mrna = 1
for aminoAcid in prot:
    mrna *= codons[aminoAcid]

mrna = 3*mrna #stop codon

print(mrna % 1000000)