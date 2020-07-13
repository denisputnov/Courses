intList = list(map(int, input().split()))
max = intList[1]
index = 0
for i in range(len(intList)):
    if intList[i] >= max:
        max = intList[i]
        index = i
print(max, index, sep=' ')
