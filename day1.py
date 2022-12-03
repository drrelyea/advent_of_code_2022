import os
from pathlib import Path

the_day = 1
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

# current_sum = 0
# max_sum = 0
# for line in data:
#     if line:
#         current_sum += int(line)
#     else:
#         max_sum = max(max_sum, current_sum)
#         current_sum = 0

current_sum = 0
all_sums = []
for line in data:
    if line:
        current_sum += int(line)
    else:
        all_sums.append(current_sum)
        current_sum = 0

max3 = sum(sorted(all_sums)[::-1][0:3])
# all_sums[0:5]
