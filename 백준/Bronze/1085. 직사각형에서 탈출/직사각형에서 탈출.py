a, b, c, d = map(int,input().split())

if 0 -a > 0:
    distancea = 0-a
else:
    distancea = a-0

if 0 -b > 0:
    distanceb = 0-b
else:
    distanceb = b-0

if a -c > 0:
    distancec = a-c
else:
    distancec = c-a

if b - d > 0:
    distanced = b-d
else:
    distanced = d-b


distance = [distancea, distanceb, distancec, distanced]
print(min(distance))
