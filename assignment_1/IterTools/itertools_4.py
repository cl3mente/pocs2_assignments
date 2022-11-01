#compress string

from itertools import groupby

S = input()
result = []
for i,j in groupby(S):
    result.append((len(list(j)), int(i)))


print(*result)
