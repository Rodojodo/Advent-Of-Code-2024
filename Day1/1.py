from utils.utils import txtTo2DWithType

lists = txtTo2DWithType("input.txt", int)
list0 = []
list1 = []
distance = 0

for i in lists:
    list0.append(i[0])
    list1.append(i[1])

for i in lists:
    x = min(list0)
    y = min(list1)
    list0.pop(list0.index(x))
    list1.pop(list1.index(y))
    distance += abs(x-y)


print(distance)