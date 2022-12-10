with open("rosalind_fibd.txt") as f:
    n,k = map(int, f.read().split())
print(n,k)

def bunny(n,k):
    if n <= 2:
        return 1
    else:
        return sum([bunny(x,k) for x in range(n-k, n-1)])


        

print(bunny(n,k))