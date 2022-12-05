import os
from pathlib import Path

the_day = 3
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

# the_sum = 0
# for line in data:
#     linelen = len(line)
#     first_set = set(line[0:int(linelen/2)])
#     second_set = set(line[int(linelen/2):])
#     intersect = first_set & second_set
#     the_char = list(intersect)[0]
#     if the_char.islower():
#         the_sum += ord(the_char) - ord('a') + 1
#     else:
#         the_sum += ord(the_char) - ord('A') + 1
# print(the_sum)

the_sum = 0
for dd in range(int(len(data)/3)):
    line1 = set(data[dd*3])
    line2 = set(data[dd*3+1])
    line3 = set(data[dd*3+2])
    intersect = line1 & line2 & line3
    the_char = list(intersect)[0]
    if the_char.islower():
        the_sum += ord(the_char) - ord('a') + 1
    else:
        the_sum += ord(the_char) - ord('A') + 1
print(the_sum)
