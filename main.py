
from assembly import assembly
from simulator import simulator

input = input("Enter your file name: ")+".txt"

# assembly instruction
instruction = []

path = 'program_instructions/'+input

t = open(path, "r")
for y in t:
    instruction.append(y)

# main

simulator(instruction, path)

