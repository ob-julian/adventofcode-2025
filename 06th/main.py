import numpy as np
from scipy.signal import convolve2d
import os
import re
#pylint: disable=missing-function-docstring

def file_reader(file_path):
    with open(os.path.join(os.path.dirname(__file__), file_path), 'r') as f:
        lines = f.read().splitlines()
        return [lines[:-1], lines[-1].replace(" ", "")]

def solver1(puzzle_input):
    np_array = np.array([re.findall("\d+", line) for line in puzzle_input[0]], dtype=np.int64) #int as datatype creates overflows
    total_sum = 0
    for i, problem in enumerate(np_array.T):
        if puzzle_input[1][i] == "+":
            total_sum += np.sum(problem)
        else:
            total_sum += np.prod(problem)
    return total_sum

def get_operator_and_neutral_element(inp):
    if inp == "+":
        return [lambda a,b : a + b, 0]
    return [lambda a,b : a * b, 1]

def solver2(puzzle_input):
    transposed =  ["".join(col) for col in zip(*puzzle_input[0])] #thx AI
    total_sum, sub_total, iterator = 0, 0, 0
    operator, sub_total = get_operator_and_neutral_element(puzzle_input[1][iterator])
    for line in transposed:
        if line.strip() == "":
            total_sum += sub_total
            iterator += 1
            operator, sub_total = get_operator_and_neutral_element(puzzle_input[1][iterator])
        else:
            sub_total = operator(sub_total, int(line))
    return total_sum + sub_total

if __name__ == "__main__":
    FILE = "input.txt"
    #FILE = "test.txt"

    INPUT = file_reader(FILE)
    print("Advent of Code: Day 6")
    print("Solution for Part 1:", solver1(INPUT))
    print("Solution for Part 2:", solver2(INPUT))
