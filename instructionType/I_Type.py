from Decimal_binary import decimal_to_binary
from label import label


def i_type(inst, opcode, path):
    labelAddr = label(path)
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
        try:
            offset = decimal_to_binary(int(inst[4]))
        except Exception as e:
            print("Error: label not found")
            exit(1)
    bitD = offset[16:32]
    result = bit0+bitA+bitB+bitC+bitD
    return result


def lw(inst, path):
    return i_type(inst, '010', path)


def sw(inst, path):
    return i_type(inst, '011', path)


def beq(inst,  addr, path):
    labelAddr = label(path)
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
        try:
            offset = decimal_to_binary(int(inst[4]))
        except Exception as e:
            print("Error: label not found")
            exit(1)
    bitD = offset[16:32]
    result = bit0+bitA+bitB+bitC+bitD
    return result
