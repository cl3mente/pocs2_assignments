with open("rosalind_rna.txt") as file:
    s = file.read()

    r = s.replace("T", "U")
    print(r)
