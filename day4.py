import os
from pathlib import Path

the_day = 4
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

# data = open(local_data_path).read().strip().split("\n")

fullycontained = 0
for line in data:
    aa,bb = line.split(",")
    aa1,aa2 =map(int,aa.split("-"))
    bb1,bb2 = map(int,bb.split("-"))
    if aa1 >= bb1 and aa2 <= bb2:
        fullycontained += 1
    elif bb1 >= aa1 and bb2 <= aa2:
        fullycontained += 1
print(fullycontained)



overlap = 0
for line in data:
    aa,bb = line.split(",")
    aa1,aa2 =map(int,aa.split("-"))
    bb1,bb2 = map(int,bb.split("-"))
    if aa2 >= bb1 and aa1 <= bb2:
        overlap += 1
    elif bb2 >= aa1 and bb1 <= aa2:
        overlap += 1
print(overlap)
