import os
from pathlib import Path
import numpy as np

the_day = 11
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

n_monkeys = 8
n_rounds = 20
monkey_items = {
    a: 0
    for a in range(n_monkeys)
}
monkey_functions = [
    lambda x: x*3,
    lambda x: x+7,
    lambda x: x+5,
    lambda x: x+8,
    lambda x: x+4,
    lambda x: x*2,
    lambda x: x+6,
    lambda x: x*x
]

monkey_tests = [
    lambda x: x % 5 == 0,
    lambda x: x % 2 == 0,
    lambda x: x % 13 == 0,
    lambda x: x % 19 == 0,
    lambda x: x % 11 == 0,
    lambda x: x % 3 == 0,
    lambda x: x % 7 == 0,
    lambda x: x % 17 == 0
]

monkey_truth = [
    2,3,5,6,3,4,7,2
]

monkey_false = [
    7,6,4,0,1,1,0,5
]

# get starting items
idata = 0
for monkey in range(n_monkeys):
    idata += 1
    item_str = data[idata].split("items: ")[1]
    items = [int(item) for item in item_str.split(', ')]
    monkey_items[monkey] = items
    idata += 6

# n_inspections = {
#     a: 0
#     for a in range(n_monkeys)
# }
# for iround in range(n_rounds):
#     for monkey in range(n_monkeys):
#         for item in monkey_items[monkey]:
#             n_inspections[monkey] += 1
#             worry_level = (monkey_functions[monkey](item) // 3)
#             test = monkey_tests[monkey](worry_level)
#             if test:
#                 monkey_items[monkey_truth[monkey]].append(worry_level)
#             else:
#                 monkey_items[monkey_false[monkey]].append(worry_level)
#         monkey_items[monkey] = []

# print(n_inspections)

biggest = 2*3*5*7*11*13*17*19
monkey_functions = [
    lambda x: x*3 % biggest,
    lambda x: x+7 % biggest,
    lambda x: x+5 % biggest,
    lambda x: x+8 % biggest,
    lambda x: x+4 % biggest,
    lambda x: x*2 % biggest,
    lambda x: x+6 % biggest,
    lambda x: x*x % biggest
]

monkey_tests = [
    lambda x: x % 5 == 0,
    lambda x: x % 2 == 0,
    lambda x: x % 13 == 0,
    lambda x: x % 19 == 0,
    lambda x: x % 11 == 0,
    lambda x: x % 3 == 0,
    lambda x: x % 7 == 0,
    lambda x: x % 17 == 0
]

n_rounds = 10000
n_inspections = np.zeros((n_monkeys, n_rounds))
item_cache = dict()
n_inspections = {
    a: 0
    for a in range(n_monkeys)
}
for iround in range(n_rounds):
    for monkey in range(n_monkeys):
        for item in monkey_items[monkey]:
            n_inspections[monkey] += 1
            worry_level = monkey_functions[monkey](item)
            test = monkey_tests[monkey](worry_level)
            if test:
                monkey_items[monkey_truth[monkey]].append(worry_level)
            else:
                monkey_items[monkey_false[monkey]].append(worry_level)
        monkey_items[monkey] = []
    # item_tuple = tuple(
    #     [
    #         a,b for a,b in monkey_items.items()
    #     ]
    # )
    # if item_tuple in item_cache:
    #     print(iround, item_tuple)
    #     break
    # item_cache[item_tuple] = iround

print(n_inspections)
