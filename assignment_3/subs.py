
with open("rosalind_subs.txt") as f:
    f = f.readlines()
    s = f[0]
    pattern = f[1]
import re


pattern = pattern.replace("\n", "")
pattern = f"(?=({pattern}))"
result = []


match = re.finditer(pattern, s)
for m in match:
    result.append(m.start(0) +1)

print(s)
print(pattern)
print(*result)