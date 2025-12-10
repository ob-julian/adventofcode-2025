import os
import numpy as np
import itertools
from pulp import LpProblem, LpVariable, LpMinimize, lpSum, LpInteger, value, PULP_CBC_CMD
#pylint: disable=missing-function-docstring

def file_reader(file_path):
    with open(os.path.join(os.path.dirname(__file__), file_path), 'r') as f:
        return [[list(int(x) for  x in line[0][1:-1].replace("#", "1").replace(".","0")), [list(int(y) for y in x[1:-1].split(",")) for x in line[1:-1]], [int(z) for z in line[-1][1:-1].split(",")]] for line in [line.split(" ") for line in f.read().splitlines()]] # 100 char line limit, thats why its just a best practice nowadays xD

def generator(length):# deprecated, use generator_optimised
    iteration = 1
    while True:
        result = bin(iteration)[2:].zfill(length)
        if len(result) > length:
            return
        yield result
        iteration += 1

def generator_optimised(n): # Thx AI, my gen function worked but was inefficient in the order it produced the needed results. With this I could shortcircute the evaluation at fist hit, shortening exec time from 1s to 0.1s
    for r in range(1, n+1):  # number of 1s in the array
        for ones_pos in itertools.combinations(range(n), r):
            arr = [0] * n
            for pos in ones_pos:
                arr[pos] = 1
            yield arr

def convert_buttons_to_matrix(length, buttons):
    matrix = [[0 for _ in range(length)] for _ in range(len(buttons))]
    for i, button in enumerate(buttons):
        for values in button:
            matrix[i][values] = 1
    return matrix


def solver1(puzzle_input):
    total = 0
    for machine in puzzle_input:
        end_state = machine[0]
        m = np.array(convert_buttons_to_matrix(len(end_state), machine[1])).T
        gen = generator_optimised(len(machine[1]))
        for item in gen:
            result = m.dot(np.array(list(item), dtype=int)) % 2
            if all(result == end_state):
                total += item.count(1)
                break
    return total

def get_sollution(buttons, result):
    prob = LpProblem("IntegerSolution", LpMinimize)

    # Generate integer variables
    x = [LpVariable(f"x{i}", lowBound=0, cat=LpInteger) for i in range(len(buttons))]

    # Objective: minimize sum of variables
    prob += lpSum(x)

    # Constraints
    actions = [[] for _ in range(len(result))]
    for i, button in enumerate(buttons):
        for active_link in button:
            actions[active_link].append(x[i])
    for i, line in enumerate(actions):
        prob += lpSum(line) == result[i]

    prob.solve(PULP_CBC_CMD(msg=False))

    if prob.status != 1:
        print("-"*50)
        print("No solution found")
        print("-"*50)
        return None  # No solution found

    solution = [value(var) for var in x]
    return solution

def solver2(puzzle_input):
    total = 0
    for machine in puzzle_input:
        end_state = machine[2]
        buttons = machine[1]
        solution = get_sollution(buttons, end_state)
        total += sum(solution) if solution is not None else 0
    return int(total)


if __name__ == "__main__":
    FILE = "input.txt"
    #FILE = "test.txt"

    INPUT = file_reader(FILE)
    print("Advent of Code: Day ")
    print("Solution for Part 1:", solver1(INPUT))
    print("Solution for Part 2:", solver2(INPUT))
