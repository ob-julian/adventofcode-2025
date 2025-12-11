import os
import igraph as ig
#pylint: disable=missing-function-docstring

def file_reader(file_path):
    with open(os.path.join(os.path.dirname(__file__), file_path), 'r') as f:
        data =  {split[0][:-1]: split[1:] for split in [line.split(" ") for line in f.read().splitlines()]}
    g = ig.Graph(directed=True)
    # Collect all unique node names (keys and targets)
    nodes = set(data.keys())
    for targets in data.values():
        nodes.update(targets)
    g.add_vertices(list(nodes))
    edges = [(key, node) for key, targets in data.items() for node in targets]
    g.add_edges(edges)
    return g

def get_numer_of_paths_between_2_points(g, n1, n2):
    return len(g.get_all_simple_paths(n1, to=n2))

def solver1(puzzle_graph):
    return get_numer_of_paths_between_2_points(puzzle_graph, "you","out")

def solver2(puzzle_graph):
    return get_numer_of_paths_between_2_points(puzzle_graph, "svr","out")
f __name__ == "__main__":
    print("Advent of Code: Day 10")
    TESTING = 0
    if TESTING:
        print("Solution for Part 1:", solver1(file_reader('test1.txt')))
        print("Solution for Part 2:", solver2(file_reader('test2.txt')))
    else:
        FILE = 'input.txt'
        INPUT = file_reader(FILE)
        print("Solution for Part 1:", solver1(INPUT))
        print("Solution for Part 2:", solver2(INPUT))
