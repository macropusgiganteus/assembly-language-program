from assembly import assembly
from Decimal_binary import *


def simulator(inst):
    print("Example Run of Simulator")

    # print instruinction
    a = 0
    mem = []
    reg = [0, 0, 0, 0, 0, 0, 0, 0]
    regA = 0
    regB = 0
    offSet = 0
    destReg = 0
    halt = 0
    count = 0

    for x in inst:
        mem.append(assembly(x, a))
        a += 1
    a = 0
    print(mem)
    print(reg)

    # print simulator
    pc = 0
    while(halt == 0):
        printState(mem, reg, pc)
        instMem = mem[pc]
        # I-type
        # lw
        if(instMem[7:10] == '010'):
            regA = binary_to_decimal(instMem[10:13])
            regB = binary_to_decimal(instMem[13:16])
            offSet = binary_to_decimal(instMem[16:32])
            reg[regB] = binary_to_decimal(mem[reg[regA] + offSet])
        # beq
        elif(instMem[7:10] == '100'):
            regA = binary_to_decimal(instMem[10:13])
            regB = binary_to_decimal(instMem[13:16])
            offSet = binary_to_decimal(instMem[16:32])
            if(reg[regA] == reg[regB]):
                pc = pc + 1 + offSet
                count += 1
                print("end state")
                continue
        # sw
        # elif(instMem[7:10] == '011'):

        # R-type
        # add
        elif(instMem[7:10] == '000'):
            regA = binary_to_decimal(instMem[10:13])
            regB = binary_to_decimal(instMem[13:16])
            destReg = binary_to_decimal(instMem[29:32])
            reg[destReg] = reg[regA] + reg[regB]
        # nand
        # elif(instMem[7:10] == '001'):

        # J-type
        # jalr
       # elif(instMem[7:10] == '101'):

        # O-type
        elif(instMem[7:10] == '110'):
            halt = 1

        pc += 1
        count += 1

        print("end state")
        if(halt == 1):
            print("machine halted")
            print("total of " + str(count) + " instructions executed")
            print("final state of machine:")


# nand(int A, int B) return string
def nand(A, B):
    binaryA = decimal_to_binary(A)
    binaryB = decimal_to_binary(B)
    binaryResult = ''
    ResultNot = ''
    bit = 0
    # A and B = Result
    while(bit < len(binaryA)):
        if(binaryA[bit] == '1' and binaryB[bit] == '1'):
            binaryResult += '1'
        else:
            binaryResult += '0'
        bit += 1
    print(binaryResult)
    # not(Result)
    bit = 0
    while(bit < len(binaryA)):
        if(binaryResult[bit] == '0'):
            ResultNot += '1'
        else:
            ResultNot += '0'
        bit += 1
    return binary_to_decimal(ResultNot)


# printState
def printState(memory, register, pc):
    regNum = 0
    print("\n@@@")
    print("state:")
    print("        pc "+str(pc))
    print("        memory:")
    for i in memory:
        print(
            "                 mem[ "+str(memory.index(i))+" ] " + str(binary_to_decimal(i)))
    print("        registors:")
    for j in register:
        print("                 reg[ "+str(regNum)+" ] " + str(j))
        regNum += 1
