from utils.utils import txtToLines
import re

lines = txtToLines("input.txt")[0]
total = 0


lines = lines.split("do()")
for i in lines:
    currentMuls = re.findall(r"mul\(\d{1,3},\d{1,3}\)", i.split("don't()")[0])
    for j in currentMuls:
        tempResult = re.findall(r"\d{1,3}", j)
        total += int(tempResult[0]) * int(tempResult[1])


print(total)
