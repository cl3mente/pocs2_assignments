#permutations

# Enter your code here. Read input from STDIN. Print output to STDOUT
from itertools import permutations

S, k = input().split()
k = int(k)

result = list(permutations(S, k))
result.sort()
for i in result:
    print(*i, sep = "")
