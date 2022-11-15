import math

with open("rosalind_prob.txt") as f:
    f = f.readlines()
    s = f[0]
    A = [float(x) for x in f[1].split()]

print(s,A)
result = []

for i in range(len(A)):
    gc_content = A[i]
    at_content = 1-gc_content
    prob_G = gc_content/2
    prob_A = at_content/2

    prob = 1
    for base in s:
        if base == "A" or base == "T":
            prob *= prob_A
        else:
            prob *= prob_G

    prob = math.log10(prob)
    result.append('{0:.4}'.format(prob))

print(*result)
    
            


