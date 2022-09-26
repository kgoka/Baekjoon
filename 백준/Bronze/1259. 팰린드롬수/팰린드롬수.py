dab1 = ""
dab2 = ""
count = 0
while 1:
    a = list(map(int,input()))
    if a[0] ==0:
        break
    elif len(a) % 2==0:
        count = len(a)
        
        for i in range(int(count/2)):
            dab1 = dab1 + str(a[i])
        for i in range(int(count - 1), int(count/2 -1), -1):
            dab2 = dab2 + str(a[i])
    elif(len(a) % 2 ==1):
        count = len(a)

        for i in range(int(count/2)):
            dab1 = dab1 + str(a[i])

        for i in range(int(count - 1), int(count/2), -1):
            dab2 = dab2 + str(a[i])

    if dab1 == dab2 :
        print("yes")
    else:
        print("no")
    dab1 = ""
    dab2 = ""
