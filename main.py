
from assembly import assembly


# assembly instruction
instruction = []
test = []
a = 0
b = 0
f = open("instruction.txt", "r")
for x in f:
    instruction.append(x)


t = open("test.txt", "r")
for y in t:
    test.append(y)

print('\n instruction file \n')
# main
for x in instruction:
    assembly(x, a)
    a += 1
a = 0

print('\ntest file jalr \n')

for y in test:
    assembly(y, b)
    b += 1
b = 0
