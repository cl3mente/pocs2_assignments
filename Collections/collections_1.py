# Default Dictionary

from collections import defaultdict

A = defaultdict(list)
B = defaultdict(list)

n,m = map(int, input().split())

for i in range(1, n+1):
    aword = input()
    A[aword].append(i)
    
for i in range(1, m+1):
    word = input()
    if word in A:
        B[word] = A[word]
    else:
        B[word].append(-1)
      
    print(*B[word], sep = " ")      
 
