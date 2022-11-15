with open("rosalind_lia.txt") as f:
    k, N = list(map(int, f.read().split()))


gentot = 2**k
print(k,N,gentot)

prob_inv = 0
for i in range(N):
    prob_AaBb = 0.25**i
    pnot_AaBb = 0.75**(gentot-i)
    prob_inv += prob_AaBb*pnot_AaBb

prob = 1-prob_inv

print('{0:.4}'.format(prob))