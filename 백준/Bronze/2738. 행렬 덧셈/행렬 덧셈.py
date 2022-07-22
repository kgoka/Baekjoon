a, b = [], []
n, m = map(int, input().split())

for i in [a, b]: 
    for j in range(n):
        i.append(list(map(int, input().split())))

for i in range(n):
    for j in range(m):
        a[i][j] = a[i][j] + b[i][j]


for i in range(n):
    print(*a[i])