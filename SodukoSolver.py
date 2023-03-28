grid = [
        [2, 5, 0,  0, 3, 0,  9, 0, 1],
        [0, 1, 0,  0, 0, 4,  0, 0, 0],
        [4, 0, 7,  0, 0, 0,  2, 0, 8],

        [0, 0, 5,  2, 0, 0,  0, 0, 0],
        [0, 0, 0,  0, 9, 8,  1, 0, 0],
        [0, 4, 0,  0, 0, 3,  0, 0, 0],

        [0, 0, 0,  3, 6, 0,  0, 7, 2],
        [0, 7, 0,  0, 0, 0,  0, 0, 3],
        [9, 0, 3,  0, 0, 0,  6, 0, 4]
]


'''
loop through all the elemenets on grid
if find 0 , try all numbers 1-9
do ifs on row, coloumn, box,
run it while there is no more 0s in the grid
'''
def find_next_empty(puzzle):

    for r in range(9):
        for c in range(9):
            if puzzle[r][c] == 0:
                return r, c

    return None, None  # if no spaces in the puzzle are empty (-1)

def num_of_zeros():
        num = []
        for x in grid:
                for y in x:
                        if y == 0:
                                num.append(y)

        return len(num)

# def populate_zero(grid, row, column):
#         rows =grid[row]
#         columns = [grid[x][column] for x in range(9)]
#
#         row_start = row//3 *3
#         col_start = column//3 *3
#         cube = []
#         for r in range(row_start, row_start + 3):
#                 for c in range(col_start , col_start+3):
#                         cube.append(grid[r][c])
#         for x in range(1,10):
#                 if x not in rows and x not in columns and x not in cube:
#                         grid[row][column] = x
#                         break
def populate_zero(grid, row, column, guess):
        rows =grid[row]
        if guess in rows:
                return False
        columns = [grid[x][column] for x in range(9)]
        if guess in columns:
                return False

        row_start = row//3 *3
        col_start = column//3 *3
        cube = []
        for r in range(row_start, row_start + 3):
                for c in range(col_start , col_start+3):
                        if(grid[r][c]) == guess:
                                return False
        return True




def solve_sudoku(grid):

    row, col = find_next_empty(grid)

    if row is None:  # this is true if our find_next_empty function returns None, None
        return True


    for guess in range(1, 10):  # range(1, 10) is 1, 2, 3, ... 9
        if populate_zero(grid, row, col, guess):
            # step 3.1: if this is a valid guess, then place it at that spot on the puzzle
            grid[row][col] = guess
            # step 4: then we recursively call our solver!
            if solve_sudoku(grid):
                return True

        # step 5: it not valid or if nothing gets returned true, then we need to backtrack and try a new number
        grid[row][col] = 0

    # step 6: if none of the numbers that we try work, then this puzzle is UNSOLVABLE!!
    return False
print(solve_sudoku(grid))

for x in range(len(grid)):
    print(grid[x])
