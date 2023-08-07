with open("rosalind_sset.txt") as f:
    n = int(f.read())

res = (2**n)%1000000
print(res)