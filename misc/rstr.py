with open('rosalind_rstr.txt') as h:
    n, GC, seq = h.read().strip().split()
    n = int(n)
    GC = float(GC)
    seq = str(seq)

print(n, GC, seq)

prob_dict = {'A': (1-GC)/2,
             'T': (1-GC)/2,
             'C': GC/2,
             'G': GC/2}


#print(prob_dict)

pG = pC = GC/2
pA = pT = (1-GC)/2


prob = 1
for base in seq:
#    print(prob_dict[base])
    prob = prob * prob_dict[base] # probability of having the EXACT same string as s given GC




prob = 1 - prob # probability of having at least one mistake

prob = (prob ** n)

prob = 1 - prob

print('{:#.3g}'.format(prob))







