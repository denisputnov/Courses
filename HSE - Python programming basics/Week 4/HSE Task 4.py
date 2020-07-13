def IsPointInSquare(x, y):
    if (-1 <= x <= 1) and (-1 <= y <= 1):
        return 'YES'
    return "NO"


a = float(input())
b = float(input())
print(IsPointInSquare(a, b))
