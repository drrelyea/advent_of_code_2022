import os
from pathlib import Path
import numpy as np

the_day = 10
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

add_values = [
    int(aa.split(" ")[1]) if "add" in aa else 0
    for aa in data
]
cycles = [
    2 if "add" in aa else 1
    for aa in data
]

pixels = np.cumsum(add_values)+1
total_cycles = np.cumsum(cycles)

current_cycle = 0
current_index = 0
hot_cycles = [20,60,100,140,180,220]
total = 0
for hot_cycle in hot_cycles:
    while current_cycle < hot_cycle:
        prior_value = pixels[current_index]
        current_index += 1
        current_cycle = total_cycles[current_index]
    total += hot_cycle*prior_value
print(total)



pixel = 1
crt_array = np.zeros((6,40))
instruction_index = 0
for cycle in range(240):
    xpos = cycle % 40
    ypos = cycle // 40
    if cycle >= total_cycles[instruction_index]:
        pixel = pixels[instruction_index]
        instruction_index+= 1
    if xpos == pixel-1 or xpos == pixel or xpos== pixel+1:
        crt_array[ypos,xpos] = 1
print(crt_array)