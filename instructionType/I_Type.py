from Decimal_binary import decimal_to_binary


labelAddr = []
f = open("instruction.txt", "r")

for x in f:
    y = x.rstrip().split(' ')
    labelAddr.append(y[0])


def i_type(inst, opcode):
    bitA = opcode  # opcode 24:22
    bitB = ''  # rs 21:19
    bitC = ''  # rt 18:16
    bitD = ''  # offset 15:0
    bit0 = '0000000'
    offset = 0
    rs = decimal_to_binary(int(inst[2]))
    bitB = rs[29:32]
    rt = decimal_to_binary(int(inst[3]))
    bitC = rt[29:32]

    if labelAddr.__contains__(inst[4]):
        offset = decimal_to_binary(labelAddr.index(inst[4]))
    else:
        offset = decimal_to_binary(int(inst[4]))
    bitD = offset[16:32]
    result = bit0+bitA+bitB+bitC+bitD
    return result


def lw(inst):
    return i_type(inst, '010')


def sw(inst):
    return i_type(inst, '011')


def beq(inst,  addr):
    opcode = '100'
    bitA = opcode  # opcode 24:22
    bitB = ''  # rs 21:19
    bitC = ''  # rt 18:16
    bitD = ''  # offset 15:0
    bit0 = '0000000'
    offset = 0
    rs = decimal_to_binary(int(inst[2]))
    bitB = rs[29:32]
    rt = decimal_to_binary(int(inst[3]))
    bitC = rt[29:32]

    if labelAddr.__contains__(inst[4]):
        if(addr > labelAddr.index(inst[4])):
            offset = decimal_to_binary(labelAddr.index(inst[4]) - addr - 1)
        else:
            offset = decimal_to_binary(labelAddr.index(inst[4]) - addr - 1)
    else:
        offset = decimal_to_binary(int(inst[4]))
    bitD = offset[16:32]
    result = bit0+bitA+bitB+bitC+bitD
    return result
