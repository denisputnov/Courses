def sum(a, b):
    a += 1
    b -= 1
    if b > 0:
        return sum(a, b)
    else:
        return a


a = int(input())
b = int(input())
if min(a, b) == 0:
    print(max(a, b))
else:
    print(sum(a, b))
