with open("rosalind_revc.txt") as f:
    s = f.read()

    r = s[::-1]

    r = r.translate(r.maketrans("ATCG", "TAGC"))

    print(s, r)