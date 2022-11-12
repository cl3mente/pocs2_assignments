with open("rosalind_iprb.txt") as file:
    k, m, n = map(int, list(file.read().split()))


t = k+n+m

prob_a = ((m*n)/(t**2-1)) + ((n**2-1)/(t**2-1)) + 1/4*((m**2-1)/(t**2-1))
prob_A = 1-prob_a

print(prob_A)