import os
import copy
#pylint: disable=missing-function-docstring
#pylint: disable=consider-using-enumerate

def file_reader(file_path):
    with open(os.path.join(os.path.dirname(__file__), file_path), 'r') as f:
        return [[int(point) for point in line.split(",")] for line in f.read().splitlines()]

def solver1(puzzle_input):
    size = 0
    for i in range(len(puzzle_input)):
        for j in range(i+1, len(puzzle_input)):
            corner1 = puzzle_input[i]
            corner2 = puzzle_input[j]
            size = max( (abs(corner1[0] - corner2[0])+1) * (abs(corner1[1] - corner2[1])+1), size)

    return size

def binary_search(arr, val):
    low = 0
    high = len(arr) - 1
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] < val:
            low = mid + 1
        elif arr[mid] > val:
            high = mid - 1
        else:
            return mid
    return (low - 1)+.5

def solver2(puzzle_input):
    # methode grid compression
    unknown_tile = 0
    unincorporated = 1
    corner = 2
    line = 3
    size_x = [float('inf'), float('-inf')]
    size_y = [float('inf'), float('-inf')]
    for x, y in puzzle_input:
        size_x = [min(size_x[0], x), max(size_x[1], x)]
        size_y = [min(size_y[0], y), max(size_y[1], y)]

    points_x = [0, size_x[0], size_x[1], size_x[1] +1]
    points_y = [0, size_y[0], size_y[1], size_y[1] +1]
    grid = [[unknown_tile] * 4 for _ in range(4)]

    for point in puzzle_input:
        x_index = binary_search(points_x, point[0])
        y_index = binary_search(points_y, point[1])
        if isinstance(x_index, float):
            x_index = int(x_index + 0.5)
            points_x.insert(x_index, point[0])
            for row in grid:
                row.insert(x_index, unknown_tile)
        if isinstance(y_index, float):
            y_index = int(y_index + 0.5)
            points_y.insert(y_index, point[1])
            grid.insert(y_index, [unknown_tile] * len(grid[0]))
        grid[y_index][x_index] = corner

    new_points = []
    for point in puzzle_input:
        x_index = points_x.index(point[0])
        y_index = points_y.index(point[1])
        new_points.append( (x_index, y_index) )

    old_point = new_points[-1]
    for point in new_points:
        for i in range( min(old_point[1], point[1]), max(old_point[1], point[1]) + 1):
            for j in range( min(old_point[0], point[0]), max(old_point[0], point[0]) + 1):
                if grid[i][j] == unknown_tile:
                    grid[i][j] = line
        old_point = point
    unincorporated_list = [(0,0)]
    while len(unincorporated_list) > 0:
        current = unincorporated_list.pop()
        grid[current[1]][current[0]] = unincorporated
        for move in [(1,1), (1,0), (1,-1), (0,1), (0,-1), (-1,1), (-1,0), (-1,-1)]:
            new_point = (current[0] + move[0], current[1] + move[1])
            try:
                if grid[new_point[1]][new_point[0]] == unknown_tile:
                    unincorporated_list.append(new_point)
            except IndexError:
                continue
    size = 0
    for i, point1 in enumerate(new_points):
        for j in range(i+1, len(new_points)):
            point2 = new_points[j]
            is_vaild = True
            # we need only to check the border lines
            for y in range( min(point1[1], point2[1]), max(point1[1], point2[1]) + 1):
                for x in [min(point1[0], point2[0]), max(point1[0], point2[0]) + 1]:
                    if grid[y][x] == unincorporated:
                        is_vaild = False
                        break
                if not is_vaild:
                    break
            if not is_vaild:
                continue
            for x in range( min(point1[0], point2[0]), max(point1[0], point2[0]) + 1):
                for y in [min(point1[1], point2[1]), max(point1[1], point2[1]) + 1]:
                    if grid[y][x] == unincorporated:
                        is_vaild = False
                        break
            if is_vaild:
                size = max( (abs(points_x[point1[0]] - points_x[point2[0]]) + 1) * (abs(points_y[point1[1]] - points_y[point2[1]]) + 1), size)
    return size


if __name__ == "__main__":
    FILE = "input.txt"
    #FILE = "test.txt"

    INPUT = file_reader(FILE)
    print("Advent of Code: Day ")
    print("Solution for Part 1:", solver1(INPUT))
    print("Solution for Part 2:", solver2(INPUT))
