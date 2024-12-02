from utils.utils import txtTo2DWithType
from utils import listEvals
import operator

levels = txtTo2DWithType("input.txt", int)
binaryArray = []

for level in levels:
    eval1 = listEvals.ascdesc(level, operator.gt) or listEvals.ascdesc(level, operator.lt)
    eval2 = True
    for i in range(len(level)-1):
        if listEvals.difference(level[i], level[i+1]) < 1 or listEvals.difference(level[i], level[i+1]) > 3:
            eval2 = False

    if eval1 and eval2:
        binaryArray.append(True)

    else:
        for j in range(0,len(level)):
            tempLevel = level.copy()
            tempLevel.pop(j)
            eval1 = listEvals.ascdesc(tempLevel, operator.gt) or listEvals.ascdesc(tempLevel, operator.lt)
            eval2 = True
            for i in range(len(tempLevel)-1):
                if listEvals.difference(tempLevel[i], tempLevel[i+1]) < 1 or listEvals.difference(tempLevel[i], tempLevel[i+1]) > 3:
                    eval2 = False
            if eval1 and eval2:
                binaryArray.append(True)
                break



print(binaryArray.count(True))
