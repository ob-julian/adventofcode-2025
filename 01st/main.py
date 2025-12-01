import os
#pylint: disable=missing-function-docstring

def file_reader(file_path):
    with open(os.path.join(os.path.dirname(__file__), file_path), 'r') as f:
        return f.read().splitlines()

def solver1(input_lines):
    operators = {
        "R": lambda a, b: (a + b) % 100,
        "L": lambda a, b: (a - b) % 100
    }
    is_zerro = 0

    position = 50
    for line in input_lines:
        direction = line[0]

        number= int(line[1:])
        position = operators[direction](position, number)
        if position == 0:
            is_zerro += 1
    return is_zerro

def solver2(input_lines):
    operators = {
        "R": lambda a, b: (a + b),
        "L": lambda a, b: (a - b)
    }
    over_zerro = 0

    position = 50
    for line in input_lines:
        direction = line[0]
        number= int(line[1:])

        # reduce to rotations betwen 0 and 100
        rotations = int(number / 100)
        if rotations > 0:
            over_zerro += rotations
            number = number % 100

        numeric_position = operators[direction](position, number)
        corrected_position = numeric_position % 100
        if position != 0 and numeric_position != corrected_position or numeric_position == 0:
            over_zerro += 1
        position = corrected_position
    return over_zerro


if __name__ == "__main__":
    FILE = "input.txt"
    #FILE = "test.txt"

    INPUT = file_reader(FILE)
    print("Advent of Code: Day 2")
    print("Solution for Part 1:", solver1(INPUT))
    print("Solution for Part 2:", solver2(INPUT))
