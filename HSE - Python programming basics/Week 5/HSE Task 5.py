n = int(input())
i = 1
if 0 < n < 10:
    for i in range(1, n + 1):
        print('+___ ', end='')
    print()
    for i in range(1, n + 1):
        print('|', i, ' / ', end='', sep='')
    print()
    for i in range(1, n + 1):
        print('|__\ ', end='')
    print()
    for i in range(1, n + 1):
        print('|    ', end='')
    print()
