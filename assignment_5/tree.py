with open("rosalind_tree.txt") as f:
    n, *adj = f.read().splitlines()
    adj = [tuple(i.split()) for i in adj]
    n = int(n)

print(n, adj)

#literally a tree has to have n-1 edges
#simple arithmetic solution

result = n - len(adj) - 1
print(result)