import os
#pylint: disable=missing-function-docstring

def file_reader(file_path):
    with open(os.path.join(os.path.dirname(__file__), file_path), 'r') as f:
        lines = f.read().splitlines()
        shapes = [[] for _ in range(6)]
        index = 0
        trees = []
        for line in lines:
            line = line.strip() # to be safe
            if line == "":
                index += 1
                continue
            if index < 6 and ":" in line:
                continue
            if index < 6:
                shapes[index].append([int(x) for x in line.replace(".","0").replace("#","1")])
            else:
                splited = line.split(": ")
                trees.append( [tuple(int(x) for x in splited[0].split("x")), [int(x) for x in splited[1].split(" ")]]) 
        return shapes, trees

def fits_without_fanagling(size, shape_indices):
    # all shapes are considered to be 3x3
    width, height = size
    amount_of_shapes = len(shape_indices)
    max_x = width // 3
    max_y = height // 3
    return amount_of_shapes <= max_x * max_y


def solver1(puzzle_input):
    shapes, trees = puzzle_input
    total = 0

    shape_sizes = [0 for _ in range(6)]
    for i, shape in enumerate(shapes):
        shape_sizes[i] = sum(row.count(1) for row in shape)

    for tree in trees:
        size, shape_indices = tree
        if size[0] * size[1] < sum(shape_sizes[i] * j for i, j in enumerate(shape_indices)):
            continue # not enough area
        if fits_without_fanagling(size, shape_indices):
            total += 1
        else:
            print("Skipping complex case for size", size, "and shapes", shape_indices)

    return total

def solver2(puzzle_input):
    return

if __name__ == "__main__":
    FILE = "input.txt"
    #FILE = "test.txt"

    INPUT = file_reader(FILE)
    print("Advent of Code: Day 12")
    print("Solution for Part 1:", solver1(INPUT))
    print("Solution for Part 2:", "Merry Christmas!")
