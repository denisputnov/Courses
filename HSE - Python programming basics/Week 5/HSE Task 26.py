intList = list(map(int, input().split()))
min = 999999999
pred = 999999999
for i in range(len(intList)):
    if intList[i] > 0:
        if intList[i] < pred:
            min = intList[i]
            pred = intList[i]
print(min)
