from itertools import product
import sys

with open("rosalind_lexf.txt") as f:
    f = f.readlines()
    symb = "".join(f[0].split())
    l = int(f[1])
    print(symb, l)

perm = product(symb, repeat=l)

with open("answer.txt", "x") as f:
    sys.stdout = f
    perm = map(list, list(perm))
    for p in perm:
        print(*p, sep="")


#itertools' product is already ordered lexicographically, with input characters order.