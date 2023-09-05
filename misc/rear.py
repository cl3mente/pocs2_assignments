def rev_set(pset = set):
    rev_set = set()
    
    for p in pset:

        p = list(p)

        

        for i in range(len(p)-1):
            for j in range(i,len(p)):

                rev = p[i:j+1][::-1]

                composite = tuple(p[:i] + rev + p[j+1:])

                rev_set.add(composite)

    return rev_set

def revdist(pset, sset, dist):

    if pset & sset:
        return dist
    

    pset_rev = rev_set(pset)
    sset_rev = rev_set(sset)

    dist += 2

    if pset & sset_rev:
        return dist-1
    if pset_rev & sset:
        return dist-1
    if pset_rev & sset_rev:
        return dist
    
    dist = revdist(pset_rev, sset_rev, dist)
    return dist

    
        

with open("rosalind_rear.txt") as h:
    
    arr = []
    res = []

    for i in h.readlines():
        

        if len(arr) == 2:

            dist = 0
            print(arr[0], arr[1])

            pset = set()
            pset.add(arr[0])
            
            sset = set()
            sset.add(arr[1])

            result = revdist(pset, sset, dist)
            print(result)
            res.append(result)

            arr = []
        else:
            line = tuple(map(int,i.split()))
            arr.append(line)
            
                 
    print(*res)