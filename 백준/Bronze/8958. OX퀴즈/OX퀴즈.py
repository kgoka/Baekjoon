n = int(input())
a = [None] *n
bonus = 0
jumsu = 0

for i in range(n):

    a[i] = list(input())
    for j in range(len(a[i])):
        if a[i][j] == 'O':
            bonus = bonus + 1
            jumsu = jumsu + bonus
        else:
            bonus = 0
    print(jumsu)
    jumsu = 0
    bonus = 0