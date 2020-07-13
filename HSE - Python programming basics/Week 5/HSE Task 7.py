n = int(input())
i = 1
a = 1
if 0 < n <= 9:
    for a in range(1, n + 1):
        for i in range(1, a + 1):
            print(i, sep='', end='')
            a += 1
        print()
