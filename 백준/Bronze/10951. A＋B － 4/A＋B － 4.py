a = []
while True:
    try:
        a.append(list(map(int, input().split())))
        print(a[0][0]+a[0][1])
        a = []
    except:
        break