def label(path):
    labelAddr = []
    CheckLabel = []
    space = 0
    f = open(path, "r")
    for x in f:
        y = x.rstrip().split(' ')
        labelAddr.append(y[0])
        # check if there is a duplicated label
        if(CheckLabel.__contains__(y[0]) == False):
            if(len(y[0]) < 1):
                CheckLabel.append(str(space))
                space += 1
            else:
                CheckLabel.append(y[0])
    if(len(labelAddr) != len(CheckLabel)):
        print('Error: found a duplicated label ')
        exit(1)
    return labelAddr
