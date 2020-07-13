a = int(input())
b = int(input())
if a < b:
    i = a
    for i in range(a, b + 1):
        print(i, end=' ')
elif a > b:
    i = b
    for i in tuple(range(a, b - 1, - 1)):
        print(i, end=' ')
elif a == b:
    print(a)
