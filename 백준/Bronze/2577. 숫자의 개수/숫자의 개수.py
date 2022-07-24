a = int(input())
b = int(input())
c = int(input())
dab = [0]*10
number = list(str(a * b * c))

for i in range(len(number)):
    for j in range(10):
        if int(number[i]) == j:
            dab[j] +=1
            
for i in range(10):
    print(dab[i])