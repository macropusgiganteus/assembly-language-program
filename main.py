
from assembly import assembly
from simulator import simulator

# assembly instruction
instruction = []
test = []
test1 = []
a = 0
b = 0

f = open("instruction.txt", "r")
for x in f:
    instruction.append(x)


t = open("test.txt", "r")
for y in t:
    test.append(y)

d = open("test1.txt", "r")
for y in d:
    test1.append(y)

print('\n instruction file \n')
# main
simulator(instruction)

#simulator(test1)

print('\ntest file jalr \n')

for y in test:
    assembly(y, b)
    b += 1
b = 0
