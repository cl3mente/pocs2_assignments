
with open("rosalind_subs.txt") as f:
    f = f.readlines()
    s = f[0]
    pattern = f[1]

result = []

for i in range(len(s)-len(pattern)):
    if s[i:i+len(pattern)] == pattern:
        result.append(i+1)

print(*result)
print(pattern, s)