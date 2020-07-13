inFile = open("input.txt", "r", encoding="utf8")
a = []
for i in inFile.read().split('\n'):
    a += i.split()
print(len(set(a)))
