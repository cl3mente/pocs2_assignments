with open("rosalind_iprb.txt") as file:
    k, m, n = map(int, list(file.read().split()))

tot = k+n+m
tot2 = tot*(tot-1)

aaxaa = (n*(n-1))/tot2
Aaxaa = (n*m)/tot2
AaxAa = 0.25 * (m*(m-1))/(tot2)
prob_a = aaxaa + Aaxaa + AaxAa

print(1-prob_a)