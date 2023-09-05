""" A prefix of a length n string s is a substring s[1:j]; a suffix of s is a substring s[k:n]

The failure array of s is an array P of length n for which P[k] is the length of the 
longest substring s[j:k] that is equal to some prefix s[1:k−j+1], 
where j cannot equal 1 (otherwise, P[k] would always equal k ). By convention, P[1]=0. """


from Bio import SeqIO

with open("rosalind_kmp.txt") as h:
    s = str(SeqIO.read(h, 'fasta').seq)

P = [0] * len(s)

for k in range(len(P)):

    for j in range(1,k+1):

        
        prefix = s[:k-j+1]

        if prefix in s[j:k+1] and len(prefix) > P[k]:
            P[k] = len(prefix)
            continue
            

print(*list(s), sep = " ")
print(*list(P), sep = " ")

# input:  C A G C A T G G T A T C A C A G C A G A G
# result: 0 0 0 1 2 0 0 0 0 0 0 1 2 1 2 3 4 5 3 0 0