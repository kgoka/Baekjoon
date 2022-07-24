a = int(input())
b = a-1
gongback = " "
for i in range(1,a+1,1):
    
    print(gongback*b+"*"*i)
    b -= 1