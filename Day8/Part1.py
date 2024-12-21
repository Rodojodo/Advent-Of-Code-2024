import utils.utils as ut

# Read input file and convert to list of lines
lines = ut.txtToLines("input.txt")
for i in range(len(lines)):
    lines[i] = list(lines[i])


# Define Antenna class and create list of Antenna objects
class Antenna:
    def __init__(self, x, y, frequency):
        self.x = x
        self.y = y
        self.frequency = frequency
arrayOfAntenni = []
for line in lines:
    for point in line:
        if not point == ".":
            arrayOfAntenni.append(Antenna(line.index(point), lines.index(line), point))


# Find anti-nodes (hidden nodes) in the grid
def findAntiNodes(antenni,lines):
    hiddenAntiNodeCount = 0
    hiddenAntiNodeCoords = []

    for i in antenni:
        for j in antenni:
            if i.frequency == j.frequency and i.x != j.x and i.y != j.y and i.frequency != "#":
                try:
                    newX = j.x - (i.x -j.x)
                    newY = j.y - (i.y -j.y)
                    if lines[newY][newX] == "." and newX >= 0 and newY >= 0 and newX < len(lines[0]) and newY < len(lines):
                        lines[newY][newX] = "#"
                    elif lines[newY][newX] != "#" and newX >= 0 and newY >= 0 and newX < len(lines[0]) and newY < len(lines) and [newX,newY] not in hiddenAntiNodeCoords:
                        hiddenAntiNodeCount += 1
                        hiddenAntiNodeCoords.append([newX,newY])
                except:
                    pass

    return lines,hiddenAntiNodeCount

# Update grid and get hidden anti-node count
lines, antiNodeCount = findAntiNodes(arrayOfAntenni,lines)

# Print grid and anti-node count
for i in lines:
    for j in i:
        if j == "#":
            antiNodeCount += 1

    s = ''.join(i)
    print(s)
print(antiNodeCount)