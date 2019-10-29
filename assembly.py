from instructionType.R_Type import *
from instructionType.I_Type import *
from instructionType.J_Type import *
from instructionType.O_Type import *
from Decimal_binary import *

# core function


def assembly(inst):
    instArray = inst.split(' ')
    result = ''
    # R_Type
    if instArray[1] == 'add':
        result = binary_to_decimal(add(instArray))
    elif instArray[1] == 'nand':
        result = binary_to_decimal(nand(instArray))

    # I_Type
    elif instArray[1] == 'lw':
        result = binary_to_decimal(lw(instArray))
    elif instArray[1] == 'sw':
        result = binary_to_decimal(sw(instArray))
    elif instArray[1] == 'beq':
        result = binary_to_decimal(beq(instArray))

    # J_Type
    elif instArray[1] == 'jalr':
        result = binary_to_decimal(jalr(instArray))

    # O_Type
    elif instArray[1] == 'halt':
        result = halt(instArray)
    elif instArray[1] == 'noop':
        result = binary_to_decimal(noop(instArray))
    else:
        result = 'Can not convert to machine language'

    print(result)
