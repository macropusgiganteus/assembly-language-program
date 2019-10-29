

def decimal_to_binary(decimal):
    binary = ''
    divide = decimal
    while divide > 0.5:
        if divide % 2 == 0:
            binary += '0'
        else:
            binary += '1'
        divide = divide/2
    return binary[::-1]


def binary_to_decimal(binary):
    decimal = 0
    lenght = len(binary)-1
    for x in binary:
        if x == '1':
            decimal += pow(2, lenght)

        lenght = lenght-1
    return decimal
