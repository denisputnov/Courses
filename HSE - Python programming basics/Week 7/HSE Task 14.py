string = ''
numbers = {}
f = open('input.txt', 'r')
for line in f:
    string = string + ' ' + line.replace('\n', '')
f.close()
for word in string.split():
    numbers[word] = numbers.get(word, 0) + 1
    print(numbers[word] - 1, end=' ')
