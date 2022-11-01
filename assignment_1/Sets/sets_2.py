# Enter your code here. Read input from STDIN. Print output to STDOUT

length = map(int, input().split())
n = map(int, input().split())
A = set(map(int, input().split()))
B = set(map(int, input().split()))

hapy = 0

for i in n:
    if i in A:
        hapy += 1
    if i in B:
        hapy -= 1
    else:
        continue

print(hapy)
