import os
import networkx as nx
#pylint: disable=missing-function-docstring

def file_reader(file_path):
    with open(os.path.join(os.path.dirname(__file__), file_path), 'r') as f:
        data =  {split[0][:-1]: split[1:] for split in [line.split(" ") for line in f.read().splitlines()]}
    dg = nx.DiGraph()
    #vertices = {}
    dg.add_nodes_from(data)
    for key, data in data.items():
        for node in data:
            dg.add_edge(key, node)
    return dg

def solver1(puzzle_graph):
    return number_of_simple_paths_no_cycles(puzzle_graph, "you","out")

def remove_nodes_after(graph, node):
    # without this function and nx all_simple_paths, I terminated after 10 minutes
    # With this function, the runtime was reduced to about 15 seconds
    # with the new memoized function, its negligible again, but still a nice function
    """ Remove all nodes that are only reachable from 'node' """
    graph_copy = graph.copy()
    queue = [node]
    while queue:
        current_node = queue.pop()
        for neighbor in list(graph_copy.successors(current_node)):
            queue.append(neighbor)
        try:
            if current_node != node:
                graph_copy.remove_node(current_node)
        except:
            pass # node already removed
    return graph_copy

def reduce_graph(graph, to):
    # this methode initially shaved of quite some runtime but after implementing memoization, the effect is negligible, run to run variance is higher than the effect of this function, so its just a keepsake now
    """ Remove all nodes that do not have a path to 'to' """
    for node in list(graph.nodes):
        if nx.has_path(graph, node, to):
            continue
        else:
            graph.remove_node(node)

def number_of_simple_paths_no_cycles(graph, start, end, memo=None):
    if memo is None:# {} is a dangerous default value, shut it pylint
        memo = {}

    # found a path
    if start == end:
        return 1

    # short circuit
    if start in memo:
        return memo[start]
    total = 0

    # depth first search
    for neighbor in graph.successors(start):
        total += number_of_simple_paths_no_cycles(graph, neighbor, end, memo)

    # dont forget to memoize...
    memo[start] = total
    return total

def solver2(puzzle_graph):
    has_path_dac_fft = nx.has_path(puzzle_graph, "dac","fft")
    has_path_fft_dac = nx.has_path(puzzle_graph, "fft","dac")

    svr_dac_graph = remove_nodes_after(puzzle_graph, "dac")
    reduce_graph(svr_dac_graph, "dac")
    svr_fft_graph = remove_nodes_after(puzzle_graph, "fft")
    reduce_graph(svr_fft_graph, "fft")
    if has_path_dac_fft and has_path_fft_dac:
        print("has_path_dac_fft and has_path_fft_dac")
        raise ValueError("Both paths exist, ambiguous solution")
    if has_path_dac_fft:
        svr_dac = number_of_simple_paths_no_cycles(svr_dac_graph, "svr","dac")
        dac_fft = number_of_simple_paths_no_cycles(svr_fft_graph, "dac","fft")
        fft_out = number_of_simple_paths_no_cycles(puzzle_graph, "fft","out")
        return svr_dac * dac_fft * fft_out
    elif has_path_fft_dac:
        svr_fft = number_of_simple_paths_no_cycles(svr_fft_graph, "svr","fft")
        fft_dac = number_of_simple_paths_no_cycles(svr_dac_graph, "fft","dac")
        dac_out = number_of_simple_paths_no_cycles(puzzle_graph, "dac","out")
        return svr_fft * fft_dac * dac_out
    return 0

if __name__ == "__main__":
    print("Advent of Code: Day 10")
    TESTING = 0
    if TESTING:
        print("Solution for Part 1:", solver1(file_reader('test1.txt')))
        print("Solution for Part 2:", solver2(file_reader('test2.txt')))
    else:
        FILE = 'input.txt'
        INPUT = file_reader(FILE)
        # print(nx.find_cycle(INPUT, source="svr")) # no cycles
        print("Solution for Part 1:", solver1(INPUT))
        print("Solution for Part 2:", solver2(INPUT))
