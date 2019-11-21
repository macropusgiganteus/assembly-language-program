from Decimal_binary import decimal_to_binary
from instructionType.labelArray import label
bitA = '0000000'


def fill(inst, path):
    labelAddr = label(path)
    bitB = '0'
    # if .fill uses symbolic address
    if labelAddr.__contains__(inst[2]):
        bitB = decimal_to_binary(labelAddr.index(inst[2]))
    else:
        bitB = decimal_to_binary(int(inst[2]))
    return bitB
