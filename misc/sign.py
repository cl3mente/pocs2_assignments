from itertools import permutations
import sys

with open("rosalind_sign.txt") as f:
    n = int(f.read())

elements = [x+1 for x in range(n)]
elements += [-x for x in elements]

combos_2 = [i for i in permutations(elements,n)]
combos = []
for i in combos_2:
    if len(tuple(map(abs, i))) == len(set(map(abs,i))):
        combos.append(i)

print(elements)
with open('answer.txt','x') as h:
    sys.stdout = h
    print(len(combos))
    for i in combos:
        print(*i)

