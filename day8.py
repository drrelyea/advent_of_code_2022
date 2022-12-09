import os
from pathlib import Path
import numpy

the_day = 8
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

ndata = numpy.zeros((len(data[0]), len(data)))
for irow, row in enumerate(data):
    for icol, col in enumerate(row):
        ndata[icol, irow] = int(data[irow][icol])

# data = open(local_data_path).read().strip().split("\n")

def visible_from_top(the_data):
    visible_array = the_data*0
    for ii in range(the_data.shape[0]):
        largest_in_row = -1
        for jj in range(the_data.shape[1]):
            if the_data[ii][jj] > largest_in_row:
                visible_array[ii][jj] = 1
                largest_in_row = the_data[ii][jj]
    return visible_array

def visible_from_bottom(the_data):
    visible_array = the_data*0
    for ii in range(the_data.shape[0]):
        largest_in_row = -1
        for jj in range(the_data.shape[1]):
            if the_data[ii][-1-jj] > largest_in_row:
                visible_array[ii][-1-jj] = 1
                largest_in_row = the_data[ii][-1-jj]
    return visible_array

def visible_from_left(the_data):
    visible_array = the_data*0
    for jj in range(the_data.shape[1]):
        largest_in_row = -1
        for ii in range(the_data.shape[0]):
            if the_data[ii][jj] > largest_in_row:
                visible_array[ii][jj] = 1
                largest_in_row = the_data[ii][jj]
    return visible_array

def visible_from_right(the_data):
    visible_array = the_data*0
    for jj in range(the_data.shape[1]):
        largest_in_row = -1
        for ii in range(the_data.shape[0]):
            if the_data[-1-ii][jj] > largest_in_row:
                visible_array[-1-ii][jj] = 1
                largest_in_row = the_data[-1-ii][jj]
    return visible_array

visible_data = visible_from_bottom(ndata) + visible_from_top(ndata) + visible_from_left(ndata) + visible_from_right(ndata)
n_visible = 0
for ii in range(ndata.shape[0]):
    for jj in range(ndata.shape[1]):
        if visible_data[ii][jj] > 0:
            n_visible += 1

print(n_visible)

def find_scenic_scores(the_data):
    max_score = 0
    for ii in range(1,the_data.shape[0]-1):
        for jj in range(1,the_data.shape[1]-1):
            height = the_data[ii][jj]
            updistance = 0
            for iup in numpy.arange(ii-1,-1,-1):
                updistance += 1
                if the_data[iup,jj] >= height:
                    break
            downdistance = 0
            for idown in numpy.arange(ii+1,the_data.shape[0]):
                downdistance += 1
                if the_data[idown,jj] >= height:
                    break
            leftdistance = 0
            for jleft in numpy.arange(jj-1,-1,-1):
                leftdistance += 1
                if the_data[ii,jleft] >= height:
                    break
            rightdistance = 0
            for jright in numpy.arange(jj+1,the_data.shape[1]):
                rightdistance += 1
                if the_data[ii,jright] >= height:
                    break
            if updistance*downdistance*leftdistance*rightdistance > max_score:
                max_score = updistance*downdistance*leftdistance*rightdistance
    return max_score

print(find_scenic_scores(ndata))
