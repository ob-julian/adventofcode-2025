import os
import copy
#pylint: disable=missing-function-docstring

def file_reader(file_path):
    with open(os.path.join(os.path.dirname(__file__), file_path), 'r') as f:
        return [list(line) for line in f.read().splitlines()]

def paint(puzzle_input, pos_y, pos_x):
    if puzzle_input[pos_y][pos_x] == ".":
        puzzle_input[pos_y][pos_x] = "|"

def solver1(puzzle_input):
    local_puzzle_input = copy.deepcopy(puzzle_input)
    positions =  [ (0, "".join(local_puzzle_input[0]).find("S")) ]
    splits = 0
    while len(positions) > 0:
        pos_y, pos_x = positions.pop()
        try:
            if local_puzzle_input[pos_y][pos_x] == "|":
                continue
        except IndexError:
            continue
        while True:
            if pos_y >= len(local_puzzle_input) - 1:
                break
            if local_puzzle_input[pos_y][pos_x] == "^":
                positions.append((pos_y, pos_x + 1))
                positions.append((pos_y, pos_x - 1))
                splits += 1
                break
            else:
                pos_y += 1
                if local_puzzle_input[pos_y][pos_x] == "|":
                    break
                paint(local_puzzle_input, pos_y, pos_x)
    return splits

def paint_enum(puzzle_input, pos_y, pos_x, adder):
    if puzzle_input[pos_y][pos_x] == ".":
        puzzle_input[pos_y][pos_x] = adder
    elif isinstance(puzzle_input[pos_y][pos_x], int):
        puzzle_input[pos_y][pos_x] += adder

def solver2(puzzle_input):
    local_puzzle_input = copy.deepcopy(puzzle_input)

    local_puzzle_input[0]["".join(local_puzzle_input[0]).find("S")] = 1
    runner = 0
    while runner < len(local_puzzle_input) -2:
        for i, point in enumerate(local_puzzle_input[runner]):
            if isinstance(point, int):
                try:
                    if local_puzzle_input[runner + 2][i] == "^":
                        paint_enum(local_puzzle_input, runner + 2, i + 1, point)
                        paint_enum(local_puzzle_input,  runner + 2, i - 1, point)
                    else:
                        paint_enum(local_puzzle_input,  runner + 2, i, point)
                except IndexError:
                    print("shoud not happen")
                    continue
        runner += 2
    return sum([x for x in local_puzzle_input[-2] if isinstance(x, int)])

if __name__ == "__main__":
    FILE = "input.txt"
    #FILE = "test.txt"

    INPUT = file_reader(FILE)
    print("Advent of Code: Day 7")
    print("Solution for Part 1:", solver1(INPUT))
    print("Solution for Part 2:", solver2(INPUT))
