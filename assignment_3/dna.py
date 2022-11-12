with open("rosalind_dna.txt", "r") as s:
    s = s.read()

    result = []
    for i in ["A", "C", "G", "T"]:
        result.append(s.count(i))

print(*result)
print(len(s))
print(sum(result))
print(s)