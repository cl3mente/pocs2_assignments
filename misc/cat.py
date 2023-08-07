def catalan_number(n):
    if n == 0:
        return 1

    catalan = [0] * (n + 1)
    catalan[0] = 1

    for i in range(1, n + 1):
        for j in range(i):
            catalan[i] += catalan[j] * catalan[i - j - 1]

    return catalan[n]

with open("rosalind_cat.txt") as h:
    seq = ""
    for line in h.readlines():
        if line.startswith(">"): continue
        seq += line.strip()

print(seq)
nA = seq.count("A")
nC = seq.count("C")        

n = len(seq) // 2
cat = catalan_number(n)

invalid = ((2*n - nA)*nA) + ((2*n - nC)*nC)

cat -= 2*invalid



print(f"length of seq is: {2*n}")
print(f"result is: {cat%1000000}")
