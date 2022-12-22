from itertools import permutations

with open("rosalind_pper.txt") as h:
    n,k = map(int, h.read().split())

print(n,k)

# in italian these are called "disposizioni semplici di classe k"
# D(n,k) = n(n-1)(n-2)...(n-(k-1))
def pper(n,k):
    result = n
    for i in range(1,k):
        result *= (n-i)
    return result

print(pper(n,k)%1000000)