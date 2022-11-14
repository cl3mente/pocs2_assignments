with open("rosalind_iev.txt") as f:
    f = f.read()
    families = list(map(int, f.split()))

print(families)
AAxAA, AAxAa, AAxaa, AaxAa, Aaxaa, aaxaa = families
tot = sum(families)*2
exp_AaxAa = 0.5 * AaxAa
exp_Aaxaa = Aaxaa
exp_aaxaa = 2*aaxaa

exp_aa = exp_AaxAa + exp_Aaxaa + exp_aaxaa
exp_A_ = tot - exp_aa

print(exp_A_)


