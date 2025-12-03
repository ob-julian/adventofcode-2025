import os
import re
#pylint: disable=missing-function-docstring

def file_reader(file_path):
    with open(os.path.join(os.path.dirname(__file__), file_path), 'r') as f:
        return f.read().splitlines()

def solver1_old(puzzle_input):
    result = 0
    for line in puzzle_input:
        int_list = [int(letter) for letter in line]

        biggest = -1
        second_biggest = -1
        for iterator, number in enumerate(int_list):
            if number > biggest and iterator != len(int_list)-1:
                biggest = number
                second_biggest = -1
            elif number > second_biggest:
                second_biggest = number
        result += biggest*10 + second_biggest
    return result

def check_size(number_array, new_number, iterator, max_itaration, position = 0):
    if number_array[position] < new_number:
        number_array[position] = new_number
        for i in range(position+1, len(number_array)):
            number_array[i] = -1
    elif position < max_itaration -1:
        check_size(number_array, new_number, iterator, max_itaration, position+1)

def solver(puzzle_input, depth):
    result = 0
    for line in puzzle_input:
        int_list = [int(letter) for letter in line]
        biggest_numbers = [-1]*depth
        for iterator, number in enumerate(int_list):
            remaining_numbers = len(int_list) - iterator
            slots_so_check = max(0, depth - remaining_numbers)
            check_size(biggest_numbers, number, iterator, depth, slots_so_check)
        for i, num in enumerate(biggest_numbers):
            result += num * 10**(depth-i-1)
    return result

def solver1(puzzle_input):
    return solver(puzzle_input, 2)

def solver2(puzzle_input):
    return solver(puzzle_input, 12)

if __name__ == "__main__":
    FILE = "input.txt"
    #FILE = "test.txt"

    INPUT = file_reader(FILE)
    print("Advent of Code: Day 3")
    print("Solution for Part 1:", solver1(INPUT))
    print("Solution for Part 2:", solver2(INPUT))
