n = int(input())

for i in range(n):
    num, s = input().split()
    num = int(num)
    dab = ''

    for j in s:
        dab += j * num
    print(dab)