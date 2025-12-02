import os
import re
#pylint: disable=missing-function-docstring

def file_reader(file_path):
    with open(os.path.join(os.path.dirname(__file__), file_path), 'r') as f:
        return [pair.split("-") for pair in f.read().strip().split(",")]


def solver(puzzle_input, regex):
    result = 0
    for pair in puzzle_input:
        for i in range(int(pair[0]), int(pair[1])+1):
            is_repeating = re.findall(regex, str(i))
            if is_repeating:
                result += i
    return result

def solver1(puzzle_input):
    return solver(puzzle_input, "^(.+)\\1$")

def solver2(puzzle_input):
    return solver(puzzle_input, "^(.+?)\\1+$")

if __name__ == "__main__":
    FILE = "input.txt"
    #FILE = "test.txt"

    INPUT = file_reader(FILE)
    print("Advent of Code: Day 2")
    print("Solution for Part 1:", solver1(INPUT))
    print("Solution for Part 2:", solver2(INPUT))
