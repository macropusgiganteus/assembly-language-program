from assembly import assembly
from Decimal_binary import *

n = 2
output = 'program_outputs/output' + str(n)+'.txt'
outputreg = 'program_outputs/outputreg' + str(n)+'.txt'


def simulator(inst, path):
    print("Example Run of Simulator", file=open(output, "a"))

    # print instruction
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
        mem.append(assembly(x, a, path))
        a += 1
    a = 0
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
                print("end state", file=open(output, "a"))
                continue
        # sw
        elif(instMem[7:10] == '011'):
            regA = binary_to_decimal(instMem[10:13])
            regB = binary_to_decimal(instMem[13:16])
            offSet = binary_to_decimal(instMem[16:32])
            mem[reg[regA] + offSet] = decimal_to_binary(reg[regB])

        # R-type
        # add
        elif(instMem[7:10] == '000'):
            regA = binary_to_decimal(instMem[10:13])
            regB = binary_to_decimal(instMem[13:16])
            destReg = binary_to_decimal(instMem[29:32])
            reg[destReg] = reg[regA] + reg[regB]
        # nand
        elif(instMem[7:10] == '001'):
            regA = binary_to_decimal(instMem[10:13])
            regB = binary_to_decimal(instMem[13:16])
            destReg = binary_to_decimal(instMem[29:32])
            reg[destReg] = nand(reg[regA], reg[regB])

        # J-type
        # jalr
        elif(instMem[7:10] == '101'):
            regA = binary_to_decimal(instMem[10:13])
            regB = binary_to_decimal(instMem[13:16])
            if(regA == regB):
                reg[regB] = pc + 1
            else:
                reg[regB] = pc + 1
                pc = reg[regA]
                count += 1
                continue

        # O-type
        elif(instMem[7:10] == '110'):
            halt = 1

        pc += 1
        count += 1
        print('executed PC:' + str(pc-1)+'  ' +
              str(count)+' instructions executed')
        print("end state", file=open(output, "a"))
        if(halt == 1):
            print("machine halted", file=open(output, "a"))
            print("total of " + str(count) + " instructions executed",
                  file=open(output, "a"))
            print("final state of machine:", file=open(output, "a"))
            print('n: '+str(reg[1]))
            print('r: '+str(reg[2]))
            print('result : '+str(reg[3]))
    printState(mem, reg, pc-1)


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
    indexaddr = 0
    print("\n@@@", file=open(output, "a"))
    print("state:", file=open(output, "a"))
    print("        pc "+str(pc), file=open(output, "a"))
    print("        memory:", file=open(output, "a"))
    for i in memory:
        if(indexaddr >= 49):
            print(
                "                 mem[ "+str(indexaddr)+" ] " + str(binary_to_decimal(i)), file=open(output, "a"))
        indexaddr += 1
    print("        registors:", file=open(output, "a"))
    for j in register:
        print("                 reg[ "+str(regNum) +
              " ] " + str(j), file=open(output, "a"))
        regNum += 1
    regNum = 0
    print("\n        pc "+str(pc), file=open(outputreg, "a"))
    for j in register:
        print("                 reg[ "+str(regNum) +
              " ] " + str(j), file=open(outputreg, "a"))
        regNum += 1
