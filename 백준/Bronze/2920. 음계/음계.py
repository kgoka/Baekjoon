a = []
a = list(map(int, input().split()))
ascending = 0
mixed = 0
descending = 0

if a[0] == 1:
    for i in range(8):
        if a[i] == i+1:
            ascending = ascending + 1
        else:
            mixed = 100


if a[0] == 8:
    for i in range(8):
        if a[i] == 8-i:
            descending = descending + 1
        else:
            mixed = 100

if ascending > descending and ascending > mixed:
    print("ascending")
elif descending > mixed:
    print("descending")
else:
    print("mixed")