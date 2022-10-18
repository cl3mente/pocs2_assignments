# Enter your code here. Read input from STDIN. Print output to STDOUT

M_size = input()
M = set(map(int, input().split()))
N_size = input()
N = set(map(int, input().split()))

s_diff = M.difference(N).union(N.difference(M))
l_diff = []

for i in s_diff:
    l_diff.append(i)
    
l_diff.sort()
#sort() changes the list object, and returns None object

for i in l_diff:
    print(i)
