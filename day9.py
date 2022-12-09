import os
from pathlib import Path

the_day = 9
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


def move_both(movedir, head, tail):
    if movedir == 'U':
        head[1] += 1
        if head[0] == tail[0]:
            if head[1] == tail[1] or head[1] == tail[1]+1:
                pass
            else:
                tail[1] = head[1]-1
        elif head[0] == tail[0] - 1 or head[0] == tail[0] + 1:
            if head[1] == tail[1] or head[1] == tail[1]+1:
                pass
            else:
                tail[1] = head[1]-1
                tail[0] = head[0]
    if movedir == 'D':
        head[1] -= 1
        if head[0] == tail[0]:
            if head[1] == tail[1] or head[1] == tail[1]-1:
                pass
            else:
                tail[1] = head[1]+1
        elif head[0] == tail[0] - 1 or head[0] == tail[0] + 1:
            if head[1] == tail[1] or head[1] == tail[1]-1:
                pass
            else:
                tail[1] = head[1]+1
                tail[0] = head[0]
    if movedir == 'R':
        head[0] += 1
        if head[1] == tail[1]:
            if head[0] == tail[0] or head[0] == tail[0]+1:
                pass
            else:
                tail[0] = head[0]-1
        elif head[1] == tail[1] - 1 or head[1] == tail[1] + 1:
            if head[0] == tail[0] or head[0] == tail[0]+1:
                pass
            else:
                tail[0] = head[0]-1
                tail[1] = head[1]
    if movedir == 'L':
        head[0] -= 1
        if head[1] == tail[1]:
            if head[0] == tail[0] or head[0] == tail[0]-1:
                pass
            else:
                tail[0] = head[0]+1
        elif head[1] == tail[1] - 1 or head[1] == tail[1] + 1:
            if head[0] == tail[0] or head[0] == tail[0]-1:
                pass
            else:
                tail[0] = head[0]+1
                tail[1] = head[1]
    return head, tail

head = [0,0]
tail = [0,0]
tailset = set()
tailset.add(tuple(tail))
for move in data:
    movenum = int(move.split(" ")[1])
    movedir = move.split(" ")[0]
    for imove in range(movenum):
        head, tail = move_both(movedir, head, tail)
        tailset.add(tuple(tail))
print(len(tailset))



# PART TWO
def move_relative(oldhead, newhead, oldtail):
    tail = oldtail.copy()
    if tail[1] == newhead[1]-2:
        tail[1] = newhead[1]-1
        if tail[0] == newhead[0] - 2:
            tail[0] = newhead[0]-1
        elif tail[0] == newhead[0] + 2:
            tail[0] = newhead[0]+1
        else:
            tail[0] = newhead[0]
    elif tail[1] == newhead[1]+2:
        tail[1] = newhead[1]+1
        if tail[0] == newhead[0] - 2:
            tail[0] = newhead[0]-1
        elif tail[0] == newhead[0] + 2:
            tail[0] = newhead[0]+1
        else:
            tail[0] = newhead[0]
    elif tail[0] == newhead[0]-2:
        tail[0] = newhead[0]-1
        if tail[1] == newhead[1] - 2:
            tail[1] = newhead[1]-1
        elif tail[1] == newhead[1] + 2:
            tail[1] = newhead[1]+1
        else:
            tail[1] = newhead[1]
    elif tail[0] == newhead[0]+2:
        tail[0] = newhead[0]+1
        if tail[1] == newhead[1] - 2:
            tail[1] = newhead[1]-1
        elif tail[1] == newhead[1] + 2:
            tail[1] = newhead[1]+1
        else:
            tail[1] = newhead[1]
    return tail

n_chains = 10
chain = dict()
for link in range(n_chains):
    chain[link] = [0,0]
tailset = set()
tailset.add(tuple(chain[8]))
for move in data:
    movenum = int(move.split(" ")[1])
    movedir = move.split(" ")[0]
    print(movenum, movedir)
    for imove in range(movenum):
        for link in range(n_chains):
            if link == 0:
                oldpos = chain[0].copy()
                if movedir=='U':
                    chain[link][1]+=1
                if movedir=='D':
                    chain[link][1]-=1
                if movedir=='L':
                    chain[link][0]-=1
                if movedir=='R':
                    chain[link][0]+=1
            else:
                tail = move_relative(oldpos, chain[link-1], chain[link])
                oldpos = chain[link].copy()
                chain[link] = tail
        tailset.add(tuple(chain[n_chains-1]))
print(len(tailset))

