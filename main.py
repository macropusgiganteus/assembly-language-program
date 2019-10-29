
from assembly import assembly


# assembly instruction
instruction = []

f = open("instruction.txt", "r")
for x in f:
    instruction.append(x)


# main
for x in instruction:
    assembly(x)
