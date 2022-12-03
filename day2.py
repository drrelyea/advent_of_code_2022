import os
from pathlib import Path

the_day = 2
download_data_path = Path("/Users/relyea/Downloads/input.txt")
local_data_path = "/Users/relyea/code/advent_of_code_2022/input"+str(the_day)+".txt"
if download_data_path.exists():
    download_data_path.rename(local_data_path)
with open(local_data_path) as input_file:
    inpstring = input_file.readlines()

data = [
    line.strip()
    for line in inpstring
]

scores = {
    'A X': 3,
    'B X': 1,
    'C X': 2,
    'A Y': 4,
    'B Y': 5,
    'C Y': 6,
    'A Z': 8,
    'B Z': 9,
    'C Z': 7
}
sum = 0
for line in data:
    sum += scores[line]
print(sum)
