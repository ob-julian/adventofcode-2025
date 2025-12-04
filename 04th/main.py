import numpy as np
from scipy.signal import convolve2d
import os
import re
#pylint: disable=missing-function-docstring

def file_reader(file_path):
    with open(os.path.join(os.path.dirname(__file__), file_path), 'r') as f:
        return np.array([list(line) for line in f.read().replace('@', '1').replace('.', '0').splitlines()], dtype=int).astype(bool)

def solver1(puzzle_input):
    kernel = np.array([
        [1, 1, 1],
        [1, 0, 1],
        [1, 1, 1]
    ])
    accespoints = convolve2d(puzzle_input, kernel, mode='same', boundary='fill', fillvalue=0)
    #Using Boolean Indexing, thx AI
    possible_possitions = accespoints[puzzle_input != 0]
    result = possible_possitions[possible_possitions < 4]
    return len(result)

def solver2(puzzle_input):
    kernel = np.array([
        [1, 1, 1],
        [1, 0, 1],
        [1, 1, 1]
    ])
    starting_roles = len(puzzle_input[puzzle_input == 1])
    grid = puzzle_input
    while True:
        accespoints = convolve2d(grid, kernel, mode='same', boundary='fill', fillvalue=0)
        possible_possitions = grid != 0
        real_accespoints = accespoints*possible_possitions
        remaining_roles = real_accespoints >= 4
        roles_removed = grid * remaining_roles
        if np.array_equal(roles_removed, grid):
            break
        grid = roles_removed
    roles_left = len(roles_removed[roles_removed == 1])
    return starting_roles - roles_left

if __name__ == "__main__":
    FILE = "input.txt"
    #FILE = "test.txt"

    INPUT = file_reader(FILE)
    print("Advent of Code: Day 4")
    print("Solution for Part 1:", solver1(INPUT))
    print("Solution for Part 2:", solver2(INPUT))
