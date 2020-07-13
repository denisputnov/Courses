inFile = open('input.txt', 'r', encoding='utf8')
outFile = open('output.txt', 'w', encoding='utf8')

lines = inFile.readlines()
for i in range(len(lines)):
    lines[i] = lines[i].strip()
lines.sort()
for i in range(len(lines)):
    first = lines[i].index(' ')
    second = lines[i].index(' ', first + 1)
    third = lines[i].index(' ', second + 1)
    lines[i] = lines[i][0:second] + lines[i][third:len(lines[i])] + '\n'

print(*lines, sep='', file=outFile)
inFile.close()
outFile.close()
