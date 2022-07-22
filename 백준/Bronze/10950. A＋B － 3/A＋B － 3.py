a = []

b = int(input())
for i in range(b):
    a.append(list(map(int, input().split())))
    print(a[i][0]+a[i][1])