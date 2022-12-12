import os
from pathlib import Path

the_day = 12
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

LOL I solved this by eye