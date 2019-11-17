
from assembly import assembly
from simulator import simulator

input = input("Enter your file name: ")+".txt"

# assembly instruction
instruction = []


t = open(input, "r")
for y in t:
    instruction.append(y)

# main
simulator(instruction)
