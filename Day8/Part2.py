import utils.utils as ut
from Part1 import Antenna

# Read input file and convert to list of lines
lines = ut.txtToLines("input.txt")
for i in range(len(lines)):
    lines[i] = list(lines[i])


# Create list of Antenna objects
antennae = []
for line in lines:
    for point in line:
        if not point == ".":
            antennae.append(Antenna(line.index(point), lines.index(line), point))


# Find anti-nodes in the grid
def findAntiNodes(antennae, lines):
    for i in antennae:
        for j in antennae:
            if i.frequency == j.frequency and i.x != j.x and i.y != j.y and i.frequency != "#":
                try:
                    newX = j.x - (i.x -j.x)
                    newY = j.y - (i.y -j.y)
                    while newX >= 0 and newY >= 0 and newX < len(lines[0]) and newY < len(lines):
                        if lines[newY][newX] == ".":
                            lines[newY][newX] = "#"
                        newX -= (i.x -j.x)
                        newY -= (i.y -j.y)
                except:
                    pass

    return lines

# Update grid
lines = findAntiNodes(antennae, lines)
antiNodeCount = 0

# Find and print anti-node count
for i in lines:
    for j in i:
        if j != ".":
            antiNodeCount += 1

print(antiNodeCount)