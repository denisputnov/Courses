intList = list(map(int, input().split()))
maxi = intList.index(max(intList))
mini = intList.index(min(intList))
dop = intList[maxi]
intList[maxi] = intList[mini]
intList[mini] = dop
print(*intList)
