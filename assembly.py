from instructionType.R_Type import *
from instructionType.I_Type import *
from instructionType.J_Type import *
from instructionType.O_Type import *
from instructionType.fill import fill
from Decimal_binary import binary_to_decimal

# core function


def assembly(inst, addr, path):
    instArray = inst.rstrip().split(' ')
    result = ''
    # R_Type
    if instArray[1] == 'add':
        result = add(instArray)
    elif instArray[1] == 'nand':
        result = nand(instArray)

    # I_Type
    elif instArray[1] == 'lw':
        result = lw(instArray, path)
    elif instArray[1] == 'sw':
        result = sw(instArray, path)
    elif instArray[1] == 'beq':
        result = beq(instArray, addr, path)

    # J_Type
    elif instArray[1] == 'jalr':
        result = jalr(instArray, addr)

    # O_Type
    elif instArray[1] == 'halt':
        result = halt(instArray)
    elif instArray[1] == 'noop':
        result = noop(instArray)
    elif instArray[1] == '.fill':
        result = fill(instArray, path)
    else:
        result = 'Can not convert to machine language'
    print('memory[' + str(addr) + '] = ' + str(binary_to_decimal(result)))
    return result
