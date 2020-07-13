myStrList = open('input.txt', encoding='utf8')
a = {}
for line in myStrList:
    words = line.strip().split()
    for word in words:
        a[word] = a.get(word, 0) + 1
print(sorted(a.items(), key=lambda x: (-x[1], x[0]))[0][0])
