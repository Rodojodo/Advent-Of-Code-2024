from utils.utils import txtToLines
import re

lines = txtToLines("input.txt")[0]
total = 0


lines = re.findall(r"mul\(\d{1,3},\d{1,3}\)", lines)
for i in lines:
    tempResult = re.findall(r"\d{1,3}", i)
    total += int(tempResult[0]) * int(tempResult[1])

print(total)
