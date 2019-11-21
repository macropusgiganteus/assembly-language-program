def label(path):
    labelAddr = []
    f = open(path, "r")
    for x in f:
        y = x.rstrip().split(' ')
        labelAddr.append(y[0])
    duplicatedLabel(labelAddr)
    return labelAddr


# check if there is a duplicated label
def duplicatedLabel(AllLabel):
    CheckLabel = []
    for l in AllLabel:
        if(l != '' and CheckLabel.__contains__(l) == False):
            CheckLabel.append(l)
    if(len(AllLabel) != len(CheckLabel)):
        print('Error: found a duplicated label ')
        exit(1)
