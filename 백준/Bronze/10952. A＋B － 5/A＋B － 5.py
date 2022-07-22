a = []
while True:
    a.append(list(map(int, input().split())))
    if a[0][0] == 0 and a[0][1] ==0:
        break
    else:
        print(a[0][0]+a[0][1])
        a = []