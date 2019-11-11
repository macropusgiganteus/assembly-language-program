from Decimal_binary import decimal_to_binary

 #Bits 31-25 
bits31_25 = '0000000'

 #Bits 24-22 opcode
opcode = ''

 #Bits 21-19 reg A (rs)
regA = ''

 #Bits 18-16 reg B (rt)
regB = ''

 #Bits 15-3
bits15_3 = '0000000000000'

 #Bits 2-0 destReg (rd)
destReg = ''


def add(inst):
    opcode = '000'

    rs = decimal_to_binary(int(inst[3])-1)
    regA = rs[len(rs)-3:len(rs)]

    rt = decimal_to_binary(int(inst[3]))
    regB = rt[len(rt)-3:len(rt)]

    rd = decimal_to_binary(int(inst[3])-1)
    destReg = rd[len(rd)-3:len(rd)]

    print(bits31_25 +' '+ opcode + ' ' + regA + ' ' + regB + ' ' + bits15_3 + ' ' + destReg + '\n')
    return bits31_25 + opcode + regA + regB + bits15_3 + destReg


def nand(inst):
    opcode = '001'

    rs = decimal_to_binary(int(inst[3])-1)
    resA = rs[len(rs)-3:len(rs)]

    rt = decimal_to_binary(int(inst[3]))
    regB = rt[len(rt)-3:len(rt)]

    rd = decimal_to_binary(int(inst[3]))
    destReg = rd[len(rd)-3:len(rd)]

    print(bits31_25 +' '+ opcode + ' ' + regA + ' ' + regB + ' ' + bits15_3 + ' ' + destReg +'\n')
    return bits31_25 + opcode + regA + regB + bits15_3 + destReg
