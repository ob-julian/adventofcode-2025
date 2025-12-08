import numpy as np
import os
from collections import Counter
import copy
#pylint: disable=missing-function-docstring

def file_reader(file_path):
    with open(os.path.join(os.path.dirname(__file__), file_path), 'r') as f:
        return [tuple(int(point) for point in line.split(",")) for line in f.read().splitlines()]

class PointGroup:
    def __init__(self, identifiere):
        self.ids= {identifiere}
        self.deprecated = False

    def append(self, point_group):
        if self is point_group:
            return False
        if self.deprecated or point_group.deprecated:
            print("illegal Acces")
        if len(point_group.ids) > len(self.ids):
            return point_group.append(self)
        old_id = next(iter(self.ids))
        self.ids.update(point_group.ids)
        point_group.deprecated = True
        return old_id, point_group

def _euclidean_distance(point1, point2):
    return np.linalg.norm(np.array(point1) - np.array(point2))

DISTANCE_CACHE = None

def get_sorted_distances(puzzle_input):
    global DISTANCE_CACHE
    if DISTANCE_CACHE is not None:
        return DISTANCE_CACHE
    distances = {}

    for i, point1 in enumerate(puzzle_input):
        for j, point2 in enumerate(puzzle_input[i+1:]):
            j = j + i + 1
            euclidean_distance = _euclidean_distance(point1, point2)
            distances[(i, j)] = euclidean_distance
    DISTANCE_CACHE = sorted(distances.items(), key=lambda item: item[1])
    return DISTANCE_CACHE

FILE = "input.txt"
def solver1(puzzle_input):
    amount_of_connectons = 10 if FILE == "test.txt" else 1000
    groups = [PointGroup(i) for i, _ in enumerate(puzzle_input)]
    reference_groups = copy.copy(groups)

    sorted_distances = get_sorted_distances(puzzle_input)

    for i in range(amount_of_connectons):
        point_pair = sorted_distances[i][0]
        group1 = groups[point_pair[0]]
        group2 = groups[point_pair[1]]
        result = group1.append(group2)
        if not result is False:
            (surviver_id, loosers) = result
            next_best_item = groups[surviver_id]
            for identifiere in loosers.ids:
                groups[identifiere] = next_best_item
    sorted_length_counts = sorted(Counter([len(group.ids) for group in reference_groups if not group.deprecated]).items(), reverse = True)
    amount = 0
    prod = 1
    for length, count in sorted_length_counts:
        for _ in range(count):
            amount +=1
            prod *= length
            if amount == 3:
                return prod

def solver2(puzzle_input):
    groups = [PointGroup(i) for i, _ in enumerate(puzzle_input)]

    sorted_distances = get_sorted_distances(puzzle_input)
    latest_connection = None
    for sorted_distance in sorted_distances:
        point_pair = sorted_distance[0] # sorted_distances itself is point_pair, distance
        group1 = groups[point_pair[0]]
        group2 = groups[point_pair[1]]
        result = group1.append(group2)
        if not result is False:
            latest_connection = point_pair
            (surviver_id, loosers) = result
            next_best_item = groups[surviver_id]
            for identifiere in loosers.ids:
                groups[identifiere] = next_best_item
    return puzzle_input[latest_connection[0]][0] * puzzle_input[latest_connection[1]][0]

if __name__ == "__main__":
    FILE = "input.txt"
    #FILE = "test.txt"

    INPUT = file_reader(FILE)
    print("Advent of Code: Day 8")
    print("Solution for Part 1:", solver1(INPUT))
    print("Solution for Part 2:", solver2(INPUT))
