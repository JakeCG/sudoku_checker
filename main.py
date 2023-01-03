# Write your solution here
def row_correct(sudoku: list, row_no: int):
    row = sudoku[row_no]
    for i in range(1, 10):
        if row.count(i) > 1:
            return False

    return True


def column_correct(sudoku: list, column_no: int):
    column = [row[column_no] for row in sudoku]
    for i in range(1, 10):
        if column.count(i) > 1:
            return False

    return True


def block_correct(sudoku: list, row_no: int, column_no: int):
    block = []
    for index in range(row_no, row_no + 3):
        for element in range(column_no, column_no + 3):
            block.append(sudoku[index][element])

    for i in range(1, 10):
        if block.count(i) > 1:
            return False

    return True


def sudoku_grid_correct(sudoku):
    # Check each row
    for i in range(9):
        if not row_correct(sudoku, i):
            return False

    # Check each column
    for i in range(9):
        if not column_correct(sudoku, i):
            return False

    # Check each block
    block_indices = [(0, 0), (0, 3), (0, 6), (3, 0), (3, 3), (3, 6), (6, 0), (6, 3), (6, 6)]
    for i, j in block_indices:
        if not block_correct(sudoku, i, j):
            return False

    # If the code reaches here, it means that the grid is correct
    return True