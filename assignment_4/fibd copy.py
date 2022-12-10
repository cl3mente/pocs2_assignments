with open("rosalind_fibd.txt") as f:
    n,k = map(int, f.read().split())
print(n,k)

def fib(n):
    if n == 1 or n == 2:
        return 1
    elif n<=0:
        return 0
    else:
        return fib(n-1) + fib(n-2)

def bunny(n,k):
    if n <= k:
        return fib(n)
    else:
        return fib(n) - (fib(n-k+1)+1)


        

print(bunny(n,k))