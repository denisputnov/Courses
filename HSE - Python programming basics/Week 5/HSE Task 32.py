lenList = int(input())
intList = list(map(int, input().split()))
num = int(input())
diff = 9999999
posNeed = -1
if intList.count(num) > 0:
    print(num)
else:
    for i in range(lenList):
        if abs(num - intList[i]) < diff:
            diff = abs(num - intList[i])
            posNeed = i
    print(intList[posNeed])
