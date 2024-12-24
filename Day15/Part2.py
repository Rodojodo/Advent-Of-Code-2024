import utils.utils as ut
from Day15.Part1 import calcBoxes
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
    if warehouse[y-1][x] in ["[","]"]:
        moveBigBoxUp(warehouse, x, y-1)

    if warehouse[y-1][x] == ".":
        warehouse[y-1][x] = warehouse[y][x]
        warehouse[y][x] = "."
    return warehouse


def bigMoveDown(warehouse, x, y):
    y = len(warehouse) - y -1
    warehouse = ut.transpose(ut.reverse2DHorizontal(ut.transpose(warehouse)))
    if warehouse[y-1][x] in ["[","]"]:
        moveBigBoxUp(warehouse, x, y-1)

    if warehouse[y-1][x] == ".":
        warehouse[y-1][x] = warehouse[y][x]
        warehouse[y][x] = "."
    warehouse = ut.transpose(ut.reverse2DHorizontal(ut.transpose(warehouse)))
    return warehouse

def moveBigBoxUp(warehouse, x, y):
    if warehouse[y][x] == "[":
        side = 1
    elif warehouse[y][x] == "]":
        side = -1
    else:
        return warehouse

    if checkMoveUpSafe(warehouse, x, y) and checkMoveUpSafe(warehouse, x+side, y):
        if warehouse[y-1][x] in ["[","]"] or warehouse[y-1][x+side] in ["[","]"]:
            moveBigBoxUp(warehouse, x, y-1)
            moveBigBoxUp(warehouse, x+side, y-1)

        warehouse[y-1][x] = warehouse[y][x]
        warehouse[y-1][x+side] = warehouse[y][x+side]
        warehouse[y][x] = warehouse[y][x+side] = "."

    return warehouse


def checkMoveUpSafe(warehouse, x, y):
    if warehouse[y][x] not in ["[", "]"]:
        return warehouse

    side = 1 if warehouse[y][x] == "[" else -1

    if warehouse[y][x] == "." or (warehouse[y-1][x] == "." and warehouse[y-1][x+side] == "."):
        return True
    elif warehouse[y-1][x] == "#" or warehouse[y-1][x+side] == "#":
        return False
    elif warehouse[y-1][x] == warehouse[y][x]:
        return checkMoveUpSafe(warehouse, x, y-1)
    else:
        return checkMoveUpSafe(warehouse, x, y-1) and checkMoveUpSafe(warehouse, x+side, y-1)

def useBigInstructions(warehouse, instructions):
    while instructions:
        [x, y] =ut.findCharIn2DArray(warehouse, "@")
        if instructions[0] == "<":
            warehouse = bigMoveLeft(warehouse, x, y)
        elif instructions[0] == ">":
            warehouse = bigMoveRight(warehouse, x, y)
        elif instructions[0] == "^":
            warehouse = bigMoveUp(warehouse, x, y)
        elif instructions[0] == "v":
            warehouse = bigMoveDown(warehouse, x, y)
        instructions.pop(0)
    return warehouse


warehouse = scaleWarehouse(ut.txtTo2DWithType("Day15/part2Warehouse.txt",str))
instructions = list(ut.removeNewLines(open("Day15/instructions.txt", "r").read()))
print(calcBoxes(useBigInstructions(warehouse, instructions), "["))