
n = input("N : ")
r = input("r : ")


def combination(n, r):
    if(r == 0 or n == r):
        return 1
    else:
        return combination(n-1, r)+combination(n-1, r-1)


print(combination(int(n), int(r)))
