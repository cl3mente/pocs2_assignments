with open("rosalind_fib.txt") as f:
    n,k = map(int, f.read().split())
print(n,k)

def bunny(n,k):
    if n <= 2:
        return 1
    else:
        return bunny(n-1, k) + k*bunny(n-2, k)

print(bunny(n,k))