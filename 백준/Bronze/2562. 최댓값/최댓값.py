dab = []
for i in range(9):
    dab.append(int(input()))
print(max(dab))

for i in range(9):
    if dab[i] == max(dab):
        print(i+1)
