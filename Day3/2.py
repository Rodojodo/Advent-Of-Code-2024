from utils.utils import txtToLines
import re

lines = txtToLines("input.txt")[0]
total = 0


lines = lines.split("do()")
for i in range(len(lines)):
    lines[i] = lines[i].split("don't()")
    lines[i] = re.findall(r"mul\(\d{1,3},\d{1,3}\)", lines[i][0])

    for j in range(len(lines[i])):
        tempResult = re.findall(r"\d{1,3}", lines[i][j])
        total += int(tempResult[0]) * int(tempResult[1])


print(total)
