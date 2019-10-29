# bit 31:25
bitA = '0000000'
# bit 24:22
bitB = ''
# bit 21:0
bitC = '0000000000000000000000'


def halt(inst):
    bitB = '110'
    print(bitA+' '+bitB+' '+bitC)
    return bitA+bitB+bitC


def noop(inst):
    bitB = '111'
    print(bitA+' '+bitB+' '+bitC)
    return bitA+bitB+bitC
