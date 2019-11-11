from Decimal_binary import decimal_to_binary

# opcode bit 24:22
bitA = '101'

# rs bit 21:19
bitB = ''

# rd bit 18:16
bitC = ''

# bit 31:25
bitD = '0000000'

# bit 15:0
bitE = '0000000000000000'


def jalr(inst, addr):
    rd = decimal_to_binary(addr+1)
    bitC = rd[len(rd)-3:len(rd)]

    rs = decimal_to_binary(int(inst[3]))
    bitB = rs[len(rs)-3:len(rs)]

    result = bitD+bitA+bitB+bitC+bitE

    return result
