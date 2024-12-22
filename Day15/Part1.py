from utils.utils import txtTo2DWithType, txtToLines

warehouse = txtToLines("testWarehouse.txt")
for i in range(len(warehouse)):
    warehouse[i] = list(warehouse[i])
instructions = txtToLines("testInstructions.txt")[0]
instruction = list(instructions)
