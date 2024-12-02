from utils.utils import txtTo2DWithType
from utils import listEvals

levels = txtTo2DWithType("input.txt", int)
binaryArray = []

for level in levels:
    eval1 = sorted(level) == level or sorted(level, reverse=True) == level
    eval2 = True
    for i in range(len(level)-1):
        if listEvals.difference(level[i], level[i+1]) < 1 or listEvals.difference(level[i], level[i+1]) > 3:
            eval2 = False

    binaryArray.append(eval1 and eval2)

print(binaryArray.count(True))
