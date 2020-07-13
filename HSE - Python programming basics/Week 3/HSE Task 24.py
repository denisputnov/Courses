def min4(a1, b1, c1, d1):
    min1 = min(min(a1, b1), min(c1, d1))
    return min1


a = int(input())
b = int(input())
c = int(input())
d = int(input())
print(min4(a, b, c, d))
