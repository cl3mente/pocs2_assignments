#designer door mat

n, m = map(int,(input().split()))

count = 1

for line in range((n)//2):
    print((count * ".|.").center(m,"-"))
    count += 2

print("WELCOME".center(m,"-"))

count -= 2
for line in range((n)//2):
    print((count * ".|.").center(m,"-"))
    count -= 2