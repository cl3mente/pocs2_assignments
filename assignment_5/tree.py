with open("rosalind_tree.txt") as f:
    n, *adj = f.read().splitlines()
    adj = [tuple(i.split()) for i in adj]

print(n, adj)