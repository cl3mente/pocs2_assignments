import itertools

with open("rosalind_seto.txt") as h:
    n, A, B = h.readlines()
    n = int(n)
    A = set([int(i) for i in A.replace("}", "").replace("{", "").strip().split(",")])
    B = set([int(i) for i in B.replace("}", "").replace("{", "").strip().split(",")])



N = set(range(1, n+1))


print(N)
print(A)
print(B)



import sys

with open("answer.txt", "x") as h:
    sys.stdout = h
    print(A.union(B))
    print(A.intersection(B))
    print(A.difference(B))
    print(B.difference(A))
    print(N.difference(A))
    print(N.difference(B))