def reverse():
    n = int(input())
    if n != 0:
        reverse()
        print(n)


print('0')
reverse()
