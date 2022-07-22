a = int(input())
hab = 0
jumsu = []
jumsu = list(map(int, input().split()))
gob = max(jumsu)
for i in range(a):
    jumsu[i] = jumsu[i]/gob*100

for i in range(a):
    hab = hab + jumsu[i]

print(hab/a)