import os
#pylint: disable=missing-function-docstring

def file_reader(file_path):
    with open(os.path.join(os.path.dirname(__file__), file_path), 'r') as f:
        lines = f.read().splitlines()
        count = 1
        result= [[],[]]
        for line in lines:
            line = line.strip()

            if line == "":
                count = 2
                continue
            if count == 1:
                result[0].append([int(x) for x in line.split("-")])
            else:
                result[1].append(int(line))
        result[0].sort()
        return result

def find_possible_fresh_list_entry(fresh_list, item_id):
    # removinf binary search worsens perfromance from 0.0015s to 0.01s =)
    return find_possible_fresh_list_entry_rec(fresh_list, item_id,0, len(fresh_list))

def find_possible_fresh_list_entry_rec(fresh_list, item_id, min_val, max_val):
    position = (min_val + max_val)//2
    if fresh_list[position][0] == item_id:
        return position
    elif fresh_list[position][0] > item_id:
        max_val = position
    else:
        min_val = position
    if abs(min_val - max_val) <= 1:
        return min_val
    return find_possible_fresh_list_entry_rec(fresh_list, item_id, min_val, max_val)


def solver1(puzzle_input):
    fresh_list = puzzle_input[0]
    is_fresh = 0
    for produce_id in puzzle_input[1]:
        list_point = find_possible_fresh_list_entry(fresh_list, produce_id)
        #list_point = 0
        while True:
            list_item = fresh_list[list_point]
            if list_item[0] <= produce_id <= list_item[1]:
                is_fresh += 1
                break # is fresh
            list_point += 1
            if list_point >= len(fresh_list):
                break # end of input
            if fresh_list[list_point][0] > produce_id:
                break # not fresh
    return is_fresh

def solver2(puzzle_input):
    biggest_fresh = 0
    total_fresh = 0
    for min_val, max_val in puzzle_input[0]:
        if min_val > biggest_fresh:
            total_fresh += max_val - min_val + 1
            biggest_fresh = max_val
        elif max_val > biggest_fresh:
            total_fresh += max_val - biggest_fresh
            biggest_fresh = max_val
    return total_fresh

if __name__ == "__main__":
    FILE = "input.txt"
    #FILE = "test.txt"

    INPUT = file_reader(FILE)
    #print(INPUT)
    print("Advent of Code: Day 5")
    print("Solution for Part 1:", solver1(INPUT))
    print("Solution for Part 2:", solver2(INPUT))
