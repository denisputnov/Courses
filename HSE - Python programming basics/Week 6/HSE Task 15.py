myFile = open("input.txt", "r", encoding="utf8")


def competition(n, k, comp):
    if n <= k:
        return 0
    elif comp[k] == comp[0]:
        return 1
    for i in range(k, 0, -1):
        if comp[i] < comp[i - 1]:
            return comp[i - 1]


a = int(myFile.readline())
intList = []
for line in myFile:
    newLine = line.split()
    if int(newLine[-1]) >= 40 and int(newLine[-2]) >= 40 \
            and int(newLine[-3]) >= 40:
        intList.append(newLine)
myFile.close()
intList.sort(key=lambda own: int(own[-1]) + int(own[-2]) + int(own[-3]))
intList.reverse()
comp = []
for i in intList:
    sum = int(i[-1]) + int(i[-2]) + int(i[-3])
    comp.append(sum)
n = len(comp)
print(competition(n, a, comp))
