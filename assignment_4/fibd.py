with open("rosalind_fibd.txt") as f:
    n,k = map(int, f.read().split())
print(n,k)

def bunny(n,k):
    if n <= 2:
        return 1
    else:
        return 2*bunny(n-1,k) - bunny(n-k,k) - bunny()
        

print(bunny(n,k))