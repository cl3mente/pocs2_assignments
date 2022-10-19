# Enter your code here. Read input from STDIN. Print output to STDOUT

from collections import Counter

X = int(input())
sizeList = list(map(int, input().split()))

N = int(input())

result = []

for i in range(N):
    size, price = map(int, input().split())
    if size in Counter(sizeList).keys():
        result.append(price)
        sizeList.remove(size)
    else:
        pass
    
print(sum(result))
