from Bio import SeqIO
with open("rosalind_sseq.txt") as h:
    s,t = SeqIO.parse(h, 'fasta')
    s,t = s.seq, t.seq
    print(s,t, sep="\n")

result = [0]
for i in range(len(t)):
    for j in range(len(s)):
        if t[i] == s[j] and j > result[-1]:
            result.append(j)
            break

result = [i+1 for i in result[1:]]
print(*result)