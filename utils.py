def txtToLines(filename):
    file = open(filename, "r")
    text = file.read()
    return text.split("\n")

def changeLType(l, newType):
    newList = []
    for i in l:
        newList.append(newType(i))
    return newList

def splitLBySpace(l):
    newList = []
    for i in l:
        newList.append(i.split(" "))
    return newList

def change2DType(l, what):
    newList = []
    for i in l:
        newList.append(changeLType(i, int))
    return newList

def txtTo2DWithType(filename, newType):
    return change2DType(splitLBySpace(txtToLines(filename)), newType)