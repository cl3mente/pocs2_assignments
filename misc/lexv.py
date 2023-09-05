import itertools
import sys

with open("rosalind_lexv.txt") as h:
    alphabet, n = h.readlines()
    alphabet = alphabet.split()
    n = int(n)


perms = []
for i in range(n+1):
    perms += [perm for perm in itertools.combinations(alphabet, i)]


with open("results.txt", "x") as h:
    sys.stdout = h
    for i in sorted(perms, key=lambda word: [alphabet.index(c) for c in word]):
        print(*i, sep = "")

