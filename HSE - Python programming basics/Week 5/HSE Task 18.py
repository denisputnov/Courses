intList = list(map(int, input().split()))
for i in range(len(intList)):
    if intList[i] % 2 != 1:
        print(intList[i], end=' ')
