s = str(input())
first = s[0:s.find(' ')]
second = s[s.find(' ') + 1:len(s)]
print(second, first, sep=' ')
