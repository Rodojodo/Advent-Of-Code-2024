from utils import utils as ut

warehouse = ut.txtTo2DWithType("warehouse.txt",str)
instructions = list(ut.removeNewLines(open("instructions.txt", "r").read()))

def moveLeft(warehouse, x, y):

    if warehouse[y][x-1] == ".":
        warehouse[y][x-1] = warehouse[y][x]
        warehouse[y][x] = "."
    elif warehouse[y][x-1] == "O":
        moveLeft(warehouse, x-1, y)
        if warehouse[y][x-1] != "O":
            warehouse[y][x-1] = warehouse[y][x]
            warehouse[y][x] = "."

    return warehouse

def moveRight(warehouse, x, y):
    return ut.reverse2DHorizontal(moveLeft(ut.reverse2DHorizontal(warehouse), len(warehouse[0]) - x - 1, y))

def moveUp(warehouse, x, y):
    return ut.transpose(moveLeft(ut.transpose(warehouse), y, x))

def moveDown(warehouse, x, y):
    return ut.transpose(moveRight(ut.transpose(warehouse), y, x))

def useInstructions(warehouse, instructions):
    while instructions:
        [x, y] =ut.findCharIn2DArray(warehouse, "@")
        if instructions[0] == "<":
            warehouse = moveLeft(warehouse, x, y)
        elif instructions[0] == ">":
            warehouse = moveRight(warehouse, x, y)
        elif instructions[0] == "^":
            warehouse = moveUp(warehouse, x, y)
        elif instructions[0] == "v":
            warehouse = moveDown(warehouse, x, y)
        instructions.pop(0)
    return warehouse


def calcBoxes(warehouse):
    boxes = ut.findObjectsIn2DArray(warehouse, "O")
    total = 0
    for i in boxes:
        total += i.x + i.y*100
    return total

print(calcBoxes(useInstructions(warehouse, instructions)))