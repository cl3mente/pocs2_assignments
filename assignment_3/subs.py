
# with open("rosalind_subs.txt") as f:
#     f = f.readlines()
#     s = f[0]
#     pattern = f[1]

import re as re

s = "AACTGTGCTAGTCGTAGTATATATGGCGGCATTATATATA"
pattern = "ATAT"

match = re.search(pattern, s)

result = match.start

print(result)