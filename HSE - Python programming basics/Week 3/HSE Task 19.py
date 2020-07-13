s = str(input())
if s.find('f') == -1:
    print('-2')
else:
    first = s.find('f')
    r = len(s) - len(s[first + 1:len(s)])
    s = s[first + 1:len(s)]
    if s.find('f') != -1:
        print(s.find('f') + r)
    else:
        print('-1')
