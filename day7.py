import os
from pathlib import Path
from dataclasses import dataclass

the_day = 7
download_data_path = Path("/Users/relyea/Downloads/input.txt")
local_data_path = "/Users/relyea/code/advent_of_code_2022/input"+str(the_day)+".txt"
if download_data_path.exists():
    download_data_path.rename(local_data_path)

# local_data_path = "/Users/relyea/code/advent_of_code_2022/input"+str(the_day)+"_test.txt"
with open(local_data_path) as input_file:
    inpstring = input_file.readlines()

data = [
    line.strip()
    for line in inpstring
]

# data = open(local_data_path).read().strip().split("\n")

@dataclass
class Fileinfo:
    files: dict
    dirs: list

SEPARATOR='/'

all_files = dict()
all_files['.'] = Fileinfo(files=dict(), dirs=list())

current_dir = '.'
iline = 0
while iline < len(data)-1:
    iline += 1
    if data[iline] == '$ ls':
        iline += 1
        while '$' not in data[iline]:
            if 'dir ' in data[iline]:
                the_dir = current_dir + SEPARATOR + data[iline].split(" ")[1]
                all_files[current_dir].dirs.append(the_dir)
                if the_dir not in all_files:
                    all_files[the_dir] = Fileinfo(files=dict(), dirs=list())
            else:
                all_files[current_dir].files[data[iline].split(" ")[1]] = int(data[iline].split(" ")[0])
            iline += 1
            if iline >= len(data):
                break
        iline -= 1
    elif 'cd ' in data[iline]:
        if data[iline].split(" ")[2] == "..":
            print('GO UP', data[iline], current_dir)
            current_dir = SEPARATOR.join(current_dir.split(SEPARATOR)[:-1])
            print('NOW', current_dir)
        else:
            print('GO DOWN', data[iline], current_dir)
            current_dir += SEPARATOR + data[iline].split(" ")[2]
            print('NOW', current_dir)

dir_sizes = dict()
sorted_dirs = sorted(all_files.keys(),key=len)[::-1]

for dir in sorted_dirs:
    dir_sizes[dir] = 0
    for file in all_files[dir].files:
        dir_sizes[dir] += all_files[dir].files[file]
    for subdir in all_files[dir].dirs:
        dir_sizes[dir] += dir_sizes[subdir]

total_size_gt_100k = 0
for dir in dir_sizes:
    if dir_sizes[dir] <= 100000:
        total_size_gt_100k += dir_sizes[dir]
print(total_size_gt_100k)

space_to_free = dir_sizes['.']-40000000
max_delete = dir_sizes['.']
for dir in dir_sizes:
    if dir_sizes[dir] < max_delete and dir_sizes[dir] > space_to_free:
        max_delete = dir_sizes[dir]
