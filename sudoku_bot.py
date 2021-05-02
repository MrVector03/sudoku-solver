import numpy as np

grid = [[2, 7, 0, 0, 0, 1, 9, 0, 0],
        [0, 0, 4, 0, 7, 0, 0, 0, 0],
        [5, 9, 0, 0, 3, 4, 0, 0, 0],
        [0, 5, 1, 0, 9, 0, 0, 0, 2],
        [3, 0, 0, 0, 0, 0, 0, 0, 7],
        [6, 0, 0, 0, 2, 0, 4, 9, 0],
        [0, 0, 0, 4, 8, 0, 0, 7, 6],
        [0, 0, 0, 0, 6, 0, 2, 0, 0],
        [0, 0, 6, 2, 0, 0, 0, 4, 8]]

"""
def create_grid():
    global grid
    nums = ['First', 'Second', 'Third', 'Fourth', 'Fifth', 'Sixth', 'Seventh', 'Eighth', 'Ninth']
    print("Type one row's numbers in one line or '0' if that tile is empty,\nafter inputting all the tiles, the algorithm will solve\nthe sudoku board you inputted.")
    grid = []
    for row in range(9):
        r = str(input(nums[row] + " row: "))
        temp_row = [i for i in r]
        grid.append(temp_row)
    print(grid)
    return grid
"""
#  Creating the main grid which will be solved


def available(y, x, number):
    global grid

    #  Checking if there is a same number in the same row
    for x_line in range(0, 9):
        if grid[y][x_line] == number:
            return False

    for y_line in range(0, 9):
        if grid[y_line][x] == number:
            return False

    #  Checking if there is a number in a 3x3 tile in the grid
    x_box = (x // 3) * 3  # Separating the grind into nin
    y_box = (y // 3) * 3

    for i in range(0, 3):
        for j in range(0, 3):
            if grid[y_box + i][x_box + j] == number:
                return False

    return True


"""
Using recursion every cell of the grid is getting filled and the sudoku board is 
being solved and continuously tested throughout the process
"""


def solve():
    global grid
    for y in range(9):
        for x in range(9):
            if grid[y][x] == 0:
                for number in range(1, 10):
                    if available(y, x, number, ):
                        grid[y][x] = number
                        solve()
                        grid[y][x] = 0  # If the grid somehow happens to not be available anymore for that number its resetting to 0
                return
    print(np.matrix(grid))


solve()
