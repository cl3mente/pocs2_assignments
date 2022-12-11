with open("rosalind_lgis.txt") as f:
    f = f.readlines()
    n = int(f[0])
    pi = list(map(int, f[1].split()))

inc = [(0,[])]*(n+1)
for i in pi:
    x,y = max(inc[:i])
    inc[i] = (x+1,y+[i])

print(*max(inc)[1])

inc = [(0,[])]*(n+1)
for i in reversed(pi):
    x,y = max(inc[:i])
    inc[i] = (x+1,y+[i])

print(*reversed(max(inc)[1]))