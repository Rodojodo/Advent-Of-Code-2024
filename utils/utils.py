from operator import indexOf


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

def txtTo2DWithType(path, newType):
    f = open(path, "r")
    data = []

    for i in f:
        data.append(changeLType(list(i.strip()), newType))

    return data


def stringTo2DWithType(string, newType):
    string = string.split("\n")
    data = []

    for i in string:
        data.append(changeLType(list(i.strip()), newType))

    return data

def removeNewLines(input):
    return ''.join(input.split("\n"))

def findCharIn2DArray(twoDArray, target):
    for i in twoDArray:
        if target in i:
            x = i.index(target)
            y = twoDArray.index(i)
    return [x,y]