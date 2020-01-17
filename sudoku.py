#sudoku solver -using backtracking where 0 means unsolved or empty

import pprint

def solve(tile):
    find = find_empty(tile)
    if not find:
        return True
    else:
        row, col = find

    for i in range(1, 10):
        if valid(tile, i, (row, col)):
            tile[row][col] = i

            if solve(tile):
                return True

            tile[row][col] = 0

    return False

def valid(tile, num, pos):
    for i in range(len(tile[0])):
        if tile[pos[0]][i] == num and pos[1] != i:
            return False

    for i in range(len(tile)):
        if tile[i][pos[1]] == num and pos[0] != i:
            return False

    box_x = pos[1] // 3
    box_y = pos[0] // 3

    for i in range(box_y*3, box_y*3 + 3):
        for j in range(box_x * 3, box_x*3 + 3):
            if tile[i][j] == num and (i, j) != pos:
                return False

    return True

def find_empty(tile):
    for i in range(len(tile)):
        for j in range(len(tile[0])):
            if tile[i][j] == 0:
                return (i, j)

    return None


board = [
    [0, 0, 0, 0, 8, 4, 0, 1, 0],
    [0, 8, 0, 0, 5, 0, 9, 0, 0],
    [1, 4, 0, 0, 0, 0, 2, 8, 5],
    [4, 0, 0, 0, 0, 3, 0, 6, 0],
    [0, 0, 6, 1, 0, 0, 0, 0, 9],
    [3, 0, 9, 8, 0, 0, 0, 0, 4],
    [0, 0, 0, 0, 0, 0, 4, 0, 1],
    [0, 0, 3, 4, 0, 0, 7, 0, 0],
    [0, 1, 0, 0, 6, 2, 3, 0, 0]
]

pp = pprint.PrettyPrinter(width = 35, compact = True)
solve(board)
pp.pprint(board)