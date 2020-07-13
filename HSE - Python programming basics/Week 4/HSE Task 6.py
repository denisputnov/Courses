def IsPointInCircle(x, y, xc, yc, r):
    if (x - xc) ** 2 + (y - yc) ** 2 <= r ** 2:
        return 'YES'
    return 'NO'


a = float(input())
b = float(input())
ac = float(input())
bc = float(input())
rc = float(input())
print(IsPointInCircle(a, b, ac, bc, rc))
