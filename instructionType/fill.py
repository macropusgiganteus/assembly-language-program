from Decimal_binary import decimal_to_binary

bitA = '0000000'


def label(path):
    labelAddr = []
    f = open(path, "r")
    for x in f:
        y = x.rstrip().split(' ')
        labelAddr.append(y[0])
    return labelAddr


def fill(inst, path):
    labelAddr = label(path)
    bitB = '0'
    # if .fill uses symbolic address
    if labelAddr.__contains__(inst[2]):
        bitB = decimal_to_binary(labelAddr.index(inst[2]))
    else:
        bitB = decimal_to_binary(int(inst[2]))
    return bitB
