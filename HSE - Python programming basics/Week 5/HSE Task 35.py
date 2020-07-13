intList = list(map(int, input().split()))
lenList = len(intList)
i = 0
while abs(lenList - i) > 1:
    dop = intList[i + 1]
    intList[i + 1] = intList[i]
    intList[i] = dop
    i += 2
print(*intList)
