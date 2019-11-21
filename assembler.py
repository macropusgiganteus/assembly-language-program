from assembly import *


input = input("Enter your file name: ")+".txt"

# assembly instruction
instruction = []

path = 'program_instructions/'+input

t = open(path, "r")
for y in t:
    instruction.append(y)


def assembler(instructions, pathF):
    output = 'assembler' + '.txt'
    Addr = 0
    for x in instructions:
        print(assembly(x, Addr, pathF), file=open(output, "a"))
        Addr += 1
    print('completed!')
    exit(0)


# main
assembler(instruction, path)
