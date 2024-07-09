def backtrack_solver(board: list[list[int]], square: int=0, verbose=False) -> list[list[int]]:
    """Accepts a representation of a given Sudoku board in memory (a list with indicies 0 to 80 of the possible values of each of the squares)
      and the current square being solved;
      returns a solved board using basic backtracking search or None if every value in square's domain has been tried"""
    # If square=81, return the board
    if verbose: print("backtrack_solver is running")
    if square == 81:
        return board
    if len(board[square]) == 1:
        result = backtrack_solver(board, square+1, verbose)
        if type(result) == list[list[int]]:
            return result
    # Pick the first available value in square's domain
    for value in board[square]:
        if verbose: print("Trying value " + str(value))
        # Check the neighbors of square to make sure this assignment is consistent, if it is not, try the next avialable value in the domain
        if not _is_consistent(board, square, value):
            continue
        # build a new board with this potential value
        new_board: list[list[int]] = list(board)
        new_board[square] = [value]
        if verbose: print_board(new_board)
        # Pass that new board to backtrack_solver to check the next square
        result = backtrack_solver(new_board, square+1, verbose)
        # If the recursive call returns a board, return that board
        if type(result) == list[list[int]]:
            return result
        # Else the recursive call returns None, try the next value in square's domain.
        if verbose: print("Backtracking!")

    # If all values of square's domain have been tried, return None
    return None


def _is_consistent(board: list[list[int]], square: int, value: int) -> bool:
    """Checks if the given board follows the rules of Sudoku, and returns whether it is or not"""
    for loc in _get_neighbors(square):
        if len(board[loc]) == 1 and board[loc][0] == value and (loc != square):
            return False
    return True

def _get_neighbors(square: int) -> list[int]:
    """Takes the index of a square in a Sudoku board and returns a list of the indicies of the neighbors of that square
    (i.e. those squares effected by the value of the given square)"""
    row = _get_row_col_block(square)[0]
    col = _get_row_col_block(square)[1]
    block = _get_row_col_block(square)[2]

    row_cells = set()
    for i in range(9):
        row_cells.add(row*9 + i)
    
    col_cells = set()
    m = col
    while m < 81:
        col_cells.add(m)
        m += 9

    block_cells = set()
    top_left_squares = [0,3,6,27,30,33,54,57,60]
    top_left_square = top_left_squares[block]
    for i in range(3):
        for j in range(3):
            block_cells.add(top_left_square+i+(9*j))
    
    all_cells = row_cells.union(col_cells).union(block_cells)
    to_ret = list(all_cells)
    return to_ret

def _get_row_col_block(square: int) -> tuple[int, int ,int]:
    """Returns the row of square, column of square, and the number of the Sudoku block square belongs to"""
    row: int = square // 9
    col: int = square %  9
    block: int = None
    if row < 3 and col < 3:
        block = 0
    elif row < 3 and col < 6:
        block = 1
    elif row < 3 and col < 9:
        block = 2
    elif row < 6 and col < 3:
        block = 3
    elif row < 6 and col < 6:
        block = 4
    elif row < 6 and col < 9:
        block = 5
    elif row < 9 and col < 3:
        block = 6
    elif row < 9 and col < 6:
        block = 7
    else:
        block = 8
    return (row, col, block)

def print_board(board: list[list[int]]):
    board_rep: str = ""
    count = 0
    for i in range(9):
        for j in range(9):
            to_print: str = board[count][0]
            if len(board[count]) > 1:
                to_print = 0
            board_rep += str(to_print) + " "
            if j == 2 or j == 5:
                board_rep += "| "
            count += 1
        board_rep += "\n"
        if i == 2 or i == 5:
            board_rep += "---------------------\n"
    print(board_rep)

# Test change