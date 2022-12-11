with open("rosalind_fibd.txt") as f:
    n,k = map(int, f.read().split())
print(n,k)

def bunny(n,k):
  by_age = [1] + [0]*(k-1)
  for i in range(n-1):
    by_age = [sum(by_age[1:])] + by_age[:-1]
    print(by_age)
  return sum(by_age)


print(bunny(n,k))