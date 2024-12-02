from utils.utils import txtTo2DWithType

lists = txtTo2DWithType("input.txt", int)
list0 = []
list1 = []
similarity = 0

for i in lists:
    list0.append(i[0])
    list1.append(i[1])

for i in range(len(lists)):
    similarity += list0[i] * list1.count(list0[i])

print(similarity)