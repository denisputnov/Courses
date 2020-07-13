from math import floor
p = int(input())
x = int(input())
y = int(input())
moneyCop = y + x * 100
adMCop = moneyCop + moneyCop * (p / 100)
print(int(adMCop // 100), floor(adMCop % 100), sep=' ')
