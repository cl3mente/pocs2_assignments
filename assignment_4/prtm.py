#create a dictionary with each symbol matches its molecular weight

with open("assignment_4/protein_mass.txt") as d:
    d = d.readlines()
    protmass = {}
    for i in d:
        aa, mass = i.split()
        mass = float(mass)
        protmass.update([(aa,mass)])
    

with open("rosalind_prtm.txt") as f:
    total = 0
    for i in f.read():
        total += protmass[i]
    print(total)
