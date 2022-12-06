with open("assignment_4/dna_codon.txt") as d:
    d = d.read().split("      ")
    table = {}
    for i in d:
        table.update({i.split()[0]: i.split()[1]})
    print(table)