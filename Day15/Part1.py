from utils import utils as ut

warehouse = ut.txtTo2DWithType("testWarehouse.txt",str)
instructions = ut.removeNewLines(open("testInstructions.txt", "r").read())

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