with open("rosalind_hamm.txt") as file:
    file = file.readlines()
    arr1 = file[0]
    arr2 = file[1]


hamming = 0

for i in range(len(arr1)):
    if arr1[i] != arr2[i]:
        hamming += 1

print(hamming)