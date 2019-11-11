from Decimal_binary import decimal_to_binary

labelAddr = []
bitA = '0000000'

f = open("instruction.txt", "r")

for x in f:
    y = x.rstrip().split(' ')
    labelAddr.append(y[0])


def fill(inst):
    bitB = '0'
    # if .fill uses symbolic address
    if labelAddr.__contains__(inst[2]):
        bitB = decimal_to_binary(labelAddr.index(inst[2]))
    else:
        bitB = decimal_to_binary(int(inst[2]))
    return bitB
