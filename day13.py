import os
from pathlib import Path

the_day = 13
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

def compare_elements(first, second):
    # print('inner', "fl", first, "sl", second)
    if type(first) == type(second) == int:
        if first < second:
            return 1
        elif second < first:
            return -1
    elif type(first) == type(second) == list:
        for ielement in range(len(first)):
            if len(second) == ielement:
                return -1
            comparison = compare_elements(first[ielement], second[ielement])
            if comparison == 1 or comparison == -1:
                return comparison
        if len(second) > len(first):
            return 1
    elif type(first) != type(second):
        if type(first) == int:
            return compare_elements([first],second)
        if type(second) == int:
            return compare_elements(first,[second])
    return 0

line_sum = 0
for index in range(0,len(data),3):
    exec('first_list='+data[index])
    exec('second_list='+data[index+1])
    isgood = compare_elements(first_list, second_list)
    if isgood != -1:
        line_sum += (index//3 + 1)
    # print("outer", first_list, second_list, isgood)

print(line_sum)

def high_level_compare(x, y):
    comparison = compare_elements(x,y)
    if comparison != 0:
        return comparison
    return 1

import functools
all_packets = []
all_packets.append([[2]])
all_packets.append([[6]])
for index in range(0,len(data),3):
    exec('first_list='+data[index])
    exec('second_list='+data[index+1])
    all_packets.append(first_list)
    all_packets.append(second_list)

sorted_packets = sorted(all_packets, key=functools.cmp_to_key(high_level_compare))

for ielement, element in enumerate(sorted_packets[::-1]):
    if element == [[2]]:
        first_element = ielement+1
    elif element == [[6]]:
        second_element = ielement+1
print(first_element,second_element,first_element*second_element)
