import utils.utils as ut
def scaleWarehouse(warehouse):
    newWarehouse = []
    for i in range(len(warehouse)):
        newWarehouse.append([])
        for j in range(len(warehouse[i])):
            if warehouse[i][j] == "#":
                newWarehouse[i].append("#")
                newWarehouse[i].append("#")
            elif warehouse[i][j] == ".":
                newWarehouse[i].append(".")
                newWarehouse[i].append(".")
            elif warehouse[i][j] == "@":
                newWarehouse[i].append("@")
                newWarehouse[i].append(".")
            elif warehouse[i][j] == "O":
                newWarehouse[i].append("[")
                newWarehouse[i].append("]")
    print(newWarehouse)
    return newWarehouse

def bigMoveLeft(warehouse, x, y):
    if warehouse[y][x-1] == ".":
        warehouse[y][x-1] = warehouse[y][x]
        warehouse[y][x] = "."
    elif warehouse[y][x-1] == "]" or warehouse[y][x-1] == "[":
        bigMoveLeft(warehouse, x-1, y)
        if warehouse[y][x-1] != "]" and warehouse[y][x-1] != "[":
            warehouse[y][x-1] = warehouse[y][x]
            warehouse[y][x] = "."

    return warehouse

def bigMoveRight(warehouse, x, y):
    return ut.reverse2DHorizontal(bigMoveLeft(ut.reverse2DHorizontal(warehouse), len(warehouse[0]) - x - 1, y))

def bigMoveUp(warehouse, x, y):

    if warehouse[y-1][x] == "[":
        bigMoveUp(warehouse, x, y-1)
        bigMoveUp(warehouse, x+1, y-1)
    elif warehouse[y-1][x] == "]":
        bigMoveUp(warehouse, x, y-1)
        bigMoveUp(warehouse, x-1, y-1)

    if warehouse[y-1][x] == ".":
        warehouse[y-1][x] = warehouse[y][x]
    warehouse[y][x] = "."
    return warehouse


def bigMoveDown(warehouse, x, y):
    pass

def moveBigBoxUp(warehouse, x, y):
    if warehouse[y][x] == "[" and warehouse[y-1][x] == "." and warehouse[y-1][x+1] == ".":
        warehouse[y-1][x] = "["
        warehouse[y-1][x+1] = "]"
        warehouse[y][x] = "."
        warehouse[y][x+1] = "."
    elif warehouse[y][x] == "]" and warehouse[y-1][x] == "." and warehouse[y-1][x-1] == ".":
        warehouse[y-1][x-1] = "["
        warehouse[y-1][x] = "]"
        warehouse[x][y] = warehouse[x-1][y] = "."
    elif warehouse[y-1][x] == '[' or warehouse[y-1][x] == ']':
        moveBigBoxUp(warehouse, x, y-1)
        if warehouse[y-1][x] != "[" and warehouse[y-1][x] != "]":
            warehouse[y-1][x] = warehouse[y][x]
            warehouse[y][x] = "."

    return warehouse
