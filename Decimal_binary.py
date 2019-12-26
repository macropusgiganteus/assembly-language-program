bitA = '0000000000000000'

# convert decimal to binary


def decimal_to_binary(decimal):
    binary = ''
    divide = decimal

    # positive value
    if(decimal >= 0):
        while divide > 0:
            if divide % 2 == 0:
                binary += '0'
            else:
                binary += '1'
            divide = int(divide/2)

    # negative value
    else:
        binary = decimal_to_binary(-decimal)
        convertedBits = ''

        # convert bit from 0 -> 1  and 1 -> 0
        for x in binary:
            if x == '0':
                convertedBits += '1'
            else:
                convertedBits += '0'

        # add 1 to convertedBits binary
        addConvertedBits = ''

        if convertedBits[len(convertedBits)-1] == '0':
            addConvertedBits = convertedBits[0:len(convertedBits)-1] + '1'
        else:
            n = len(convertedBits)-1
            carryOut = 1

            while n >= 0:
                if carryOut > 0:
                    if convertedBits[n] == '1':
                        addConvertedBits += '0'
                    else:
                        addConvertedBits += '1'
                        carryOut = 0
                else:
                    addConvertedBits += convertedBits[n]
                n -= 1
        if(decimal % 2 == 1):
            return addConvertedBits
        return addConvertedBits[::-1]
    if(len(binary) > 16):
        print('Error: offset field is over 16 bits')
        exit(1)
    while len(binary) != 16:
        binary = binary + '0'

    binary += bitA
    return binary[::-1]


# Convert binary to decimal
def binary_to_decimal(binary):
    decimal = 0
    count = len(binary)-1

    # positive
    for x in binary:
        if x == '1':
            # result += 2^count
            decimal += pow(2, count)

        count -= 1

    # negative
    if(binary[0] == '1'):
        revBinary = binary[::-1]
        decimal = -1
        n = 0
        while n < len(binary):
            if revBinary[n] == '0':
                decimal -= pow(2, n)
            n += 1
    return decimal
