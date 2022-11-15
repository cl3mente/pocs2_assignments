from Bio import SeqIO

seq = SeqIO.parse("rosalind_cons.txt", "fasta")
seqlist = [str(s.seq) for s in seq]
# print(seqlist)

profile = [[0 for j in range(len(seqlist[0]))] for i in range(4)]
# print(profile)

for s in seqlist:
    # print(s)
    for i in range(len(s)):
        if s[i] == "A":
            profile[0][i] +=1 #A
        if s[i] == "C":
            profile[1][i] +=1 #C
        if s[i] == "G":    
            profile[2][i] +=1 #G
        if s[i] == "T":
            profile[3][i] +=1 #T

for i in range(4):
    profile[i] = list(map(str, profile[i]))
# print(profile)

consensus = []
for i in range(len(profile[0])):
    scan = [profile[j][i] for j in range(4)]
    if max(scan) == scan[0]:
        consensus.append("A")
        continue
    if max(scan) == scan[1]:
        consensus.append("C")
        continue
    if max(scan) == scan[2]:
        consensus.append("G")
        continue
    if max(scan) == scan[3]:
        consensus.append("T")
        continue


with open("cons_answer.txt", "x") as file:

    file.write("".join(consensus) + "\n")
    file.write("A: " + " ".join(profile[0]) + "\n")
    file.write("C: " + " ".join(profile[1]) + "\n")
    file.write("G: " + " ".join(profile[2]) + "\n")
    file.write("T: " + " ".join(profile[3]))