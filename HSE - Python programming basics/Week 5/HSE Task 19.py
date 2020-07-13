intList = list(map(int, input().split()))
num = 0
for i in range(len(intList)):
    if intList[i] > 0:
        num += 1
print(num)
