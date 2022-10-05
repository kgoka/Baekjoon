count = int(input())
word = []
for i in range(count-1):
    word.append(input())

word.append(input())

word.sort()
word.sort(key = len)


for i in range(count):
    if i == count-1:
        print(word[i])
    elif word[i] == word[i+1]: 
        continue
    else:
        print(word[i])