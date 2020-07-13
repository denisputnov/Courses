intList = list(map(int, input().split()))
num = 0
for i in range(len(intList)):
    if i > 0:
        if intList[i] > intList[i-1]:
            print(intList[i], end=' ')
