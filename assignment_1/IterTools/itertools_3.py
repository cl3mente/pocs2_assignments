#Combinations

from itertools import combinations as cmb

S, k = input().split()
k = int(k)

Slist = []
for i in S:
    Slist.append(i)

Slist.sort()

for i in range(1,k+1):
    result = list(cmb(Slist,i))
    result.sort()
    for j in result:
        print(*j, sep = "")