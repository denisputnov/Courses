n = int(input())
sumSeq = 0
i = 1
while i <= n:
    sumSeq += (1 / i ** 2)
    i += 1
print(sumSeq)
