# Ordered Dictionary

from collections import OrderedDict

N = int(input())
OrdDict = OrderedDict()
for i in range(N):
    line = input().split()
    key = ""
    value = 0
    for word in line:
        if word.isdigit() == False:
            word.strip()
            if key != "":
                key = key + " " + word
            else:
                key = word
        else:
            if key in OrdDict.keys():
                value = OrdDict[key] + int(word)
            else:
                value = int(word)
            
    OrdDict[key] = value        
            

for i in OrdDict.keys():
    print(i, OrdDict[i])
        
