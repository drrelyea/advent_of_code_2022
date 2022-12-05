import os
from pathlib import Path

the_day = 5
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

moves = [
    line for line in data if "move" in line
]

initial_crates = [
    line for line in data if '[' in line
]

# dying of shame that it took me this long to invert the arrays... sigh
# ok apparently I was the only person who bothered to do this not by hand, so less shame
# what speed coding competition?
n_slots = 9
initial_crate_array = []
for line in initial_crates:
    newline = []
    for islot in range(n_slots):
        if len(line) > islot*4+1:
            newline.append(line[islot*4+1])
        else:
            newline.append(" ")
    initial_crate_array.append(newline)

transpose_array_backwards = []
for islot in range(len(initial_crate_array[0])):
    transpose_array_backwards.append([])
for layer in initial_crate_array:
    for ielement, element in enumerate(layer):
        if element != " ":
            transpose_array_backwards[ielement].append(element)
transpose_array = [
    row[::-1]
    for row in transpose_array_backwards
]

def move_crates(arr, num, start, end):
    for _ in range(num):
        arr[end-1].append(arr[start-1].pop())
    return arr

for move in moves:
    number_to_move = int(move.split(' from')[0].split('move ')[1])
    first_stack = int(move.split(' to')[0].split('from ')[1])
    second_stack = int(move.split('to ')[1])
    transpose_array = move_crates(transpose_array, number_to_move, first_stack, second_stack)

print("".join([line[-1] for line in transpose_array]))

transpose_array = [
    row[::-1]
    for row in transpose_array_backwards
]

def move_crates_no_reverse(arr, num, start, end):
    arr[end-1] += arr[start-1][-num:]
    arr[start-1] = arr[start-1][:-num]
    return arr

for move in moves:
    number_to_move = int(move.split(' from')[0].split('move ')[1])
    first_stack = int(move.split(' to')[0].split('from ')[1])
    second_stack = int(move.split('to ')[1])
    transpose_array = move_crates_no_reverse(transpose_array, number_to_move, first_stack, second_stack)
    print(move)
    for line in transpose_array:
        print(line)
    print("")

print("".join([line[-1] for line in transpose_array]))
