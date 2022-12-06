from itertools import permutations
import sys

with open("rosalind_perm.txt") as f:
    n = f.read().strip()
    n = int(n)

array = list(range(1,n+1))

perms = permutations(array)
perms = list(perms)

with open("answer.txt", "w") as f:
    sys.stdout = f
    print(str(len(perms)))
    for p in perms:
        p = list(p)
        print(*p, sep=" ")
