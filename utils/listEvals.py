def ascdesc(list, relate):
    isOrdered = True
    for i in range(len(list)-1):
        if not(relate(list[i], list[i+1])):
            isOrdered = False
    return isOrdered

def difference(int1, int2):
    return abs(int1 - int2)