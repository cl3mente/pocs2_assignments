# Enter your code here. Read input from STDIN. Print output to STDOUT

size_n = int(input())

N = set()

for i in range(size_n):
    N.add(input())    
print(len(N))
