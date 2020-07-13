intList = list(map(int, input().split()))
s = intList[0]
n = intList[1]
a = []
numUser = 0
sumUser = 0
pukUser = 0
while numUser < n:
    vUser = int(input())
    numUser += 1
    a.append(vUser)
a.sort()
for i in a:
    if sumUser < s:
        sumUser += i
        if sumUser < s:
            pukUser += 1
print(pukUser)
