import math

with open("rosalind_prob.txt") as f:
    f = f.readlines()
    s = f[0]
    A = [float(x) for x in f[1].split()]

print(s.strip(),A)
result = []

for i in A:
    GC = i
    AT = 1-i
    probG = GC/2
    probA = AT/2

    prob = 1

    for base in s:
        if base == "A" or base == "T":
            prob *= probA
        if base == "G" or base == "C":
            prob *= probG

    prob = math.log10(prob)
    result.append(prob)

    
print(*result)
with open("rosalind_prob_sol.txt", "x") as f:
    print(*result, file=f)


            


