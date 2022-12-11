with open("rosalind_lgis.txt") as f:
    f = f.readlines()
    n = int(f[0])
    pi = list(map(int, f[1].split()))

arr = [(0,[])]*(n+1)
for i in pi:
    x,y = max(arr[:i])
    arr[i] = (x+1,y+[i])

print(*max(arr)[1])

arr = [(0,[])]*(n+1)
for i in reversed(pi):
    x,y = max(arr[:i])
    arr[i] = (x+1,y+[i])

print(*reversed(max(arr)[1]))