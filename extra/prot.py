with open("assignment_4/rna_codon_table.txt") as d:
    d = d.read().split("      ")
    table = {}
    for i in d:
        table.update({i.split()[0]: i.split()[1]})
    print(table)

with open("rosalind_prot.txt") as f:
    f = f.read().strip()

result = ""
codon = ""
for i in f:
    if len(codon) == 3:
        result += table[codon]
        if codon in ["UAG", "UGA", "UAA"]:
            break
        else:
            codon = ""

    codon += i

print(result)