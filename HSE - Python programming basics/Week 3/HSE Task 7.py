from math import floor
p = int(input())
x = int(input())
y = int(input())
k = int(input())
i = 1
moneyCop = y + x * 100
adMCop = moneyCop
while i <= k:
    adMCop = int(adMCop + adMCop * (p / 100))
    i += 1
print(int(adMCop // 100), floor(adMCop % 100), sep=' ')
