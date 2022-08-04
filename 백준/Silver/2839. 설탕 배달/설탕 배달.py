sugar = int(input())

bongji = 0
while sugar >= 0 :
    if sugar % 5 == 0 : 
        bongji += (sugar // 5)
        print(bongji)
        break
    sugar -= 3  
    bongji += 1  
else :
    print(-1)
