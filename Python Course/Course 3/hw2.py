import re
fh = open('hw2.txt')
numlist = []
for line in fh:
    line = line.rstrip()
    a = re.findall('[0-9]+', line)
    if len(a) ==0  : continue
    for i in range(len(a)):
        a[i] = int(a[i])
    numlist = numlist + a
print(numlist)
print(len(numlist))
print(sum(numlist))



