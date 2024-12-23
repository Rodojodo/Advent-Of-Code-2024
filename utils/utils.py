
def txtToLines(filename):
    file = open(filename, "r")
    text = file.read()
    file.close()
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

    f.close()
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
    x=-1
    y=-1
    for i in twoDArray:
        if target in i:
            x = i.index(target)
            y = twoDArray.index(i)
    return [x,y]


def reverse2DHorizontal(twoDArray):
    data = []
    for i in twoDArray:
        data.append(i[::-1])
    return data


def transpose(l1):
    data = []

    # iterate over list l1 to the length of an item
    for i in range(len(l1[0])):
        # print(i)
        row =[]
        for item in l1:
            # appending to new list with values and index positions
            # i contains index position and item contains values
            row.append(item[i])
        data.append(row)
    return data


def findObjectsIn2DArray(twoDArray, target):
    class Coords:
        def __init__(self, x, y):
            self.x = x
            self.y = y

    objects = []
    for i in range(len(twoDArray)):
        for j in range(len(twoDArray[i])):
            if twoDArray[i][j] == target:
                objects.append(Coords(j,i))

    return objects