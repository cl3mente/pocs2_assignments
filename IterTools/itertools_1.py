#product

from itertools import product

A = list(map(int, input().split()))
B = list(map(int, input().split()))

product = list(product(A,B))
print(*product)
#asterisk unwraps an iterable