import numpy as np

with open('rosalind_eval.txt') as h:
    n, s, *A = h.read().strip().split()
    n = int(n)
    s = str(s)
    A = list(map(float, list(A)))


print(n, s, A, sep = "\n")


'''
An array B having the same length as A in which B[i] represents the expected number of times 
that s will appear as a substring of a random DNA string t of length n, where t is formed with GC-content A[i]
'''

B = []
for GC in A:
    prob_dict = {'A': (1-GC)/2,
             'T': (1-GC)/2,
             'C': GC/2,
             'G': GC/2}
    
    prob = np.prod([prob_dict[i] for i in s])

    B.append(prob * (n - len(s) + 1))


print(*B, sep = " ")

    

