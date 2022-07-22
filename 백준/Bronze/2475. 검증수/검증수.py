gum = []
gum = list(map(int, input().split()))
dab = 0 
for i in range(5):
    dab = gum[i]**2 + dab

print(dab%10)