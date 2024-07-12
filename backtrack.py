def backtrack_solver(board: list[list[int]], square: int=0, verbose=False) -> list[list[int]]:
    """Accepts a representation of a given Sudoku board in memory (a list with indicies 0 to 80 of the possible values of each of the squares)
      and the current square being solved;
      returns a solved board using basic backtracking search or None if every value in square's domain has been tried"""

    # If square=81, return the board
    if verbose: print(f"backtrack_solver is running on square number {square}")
    if square == 81:
        return board

    # # If the square already has a value, don't try to change it
    # if len(board[square]) == 1:
    #     if verbose: print("    This square is already solved")
    #     result = backtrack_solver(board, square+1, verbose)

    #     # If the result is a board, keep passing it back down the stack
    #     if type(result) == list[list[int]]:
    #         return result
    
    if verbose: print(board[square]) # print square's domain

    # Pick the first available value in square's domain
    for value in board[square]:
        # build a new board with this potential value
        new_board: list[list[int]] = list(board)
        new_board[square] = [value]

        if verbose: print("Trying value " + str(value))
        if verbose: print_board(new_board)

        # Check the neighbors of square to make sure this assignment is consistent,
        # if it is not, try the next avialable value in the domain
        if not _is_consistent(board, square, value):
            continue

        # use forward checking to determine if this value is viable in the longer term
        if not _forward_check(new_board, square, value):
            continue

        if verbose: print_board(new_board)

        # Pass that new board to backtrack_solver to check the next square
        result = backtrack_solver(new_board, square+1, verbose)

        # If the recursive call returns a board, return that board
        if type(result) == list[list[int]]:
            return result
        
        # Else the recursive call returns None, try the next value in square's domain.
        continue

    # If all values of square's domain have been tried, return None
    if verbose: print(f"Backtracking to square number {square - 1}")
    return None


def _is_consistent(board: list[list[int]], square: int, value: int) -> bool:
    """Checks if the given board follows the rules of Sudoku, and returns whether it is or not"""
    for loc in _get_neighbors(square):
        #print("Checking the value of square number " + str(loc) + "(" + str(board[loc]) + ")" + " against the value of square number " + str(square) + "(" + str(value) + ")")
        if len(board[loc]) == 1 and board[loc][0] == value and (loc != square):
            print("There is a " + str(board[loc][0]) + " in square " + str(loc) + " that conflicts with the " + str(value) + " in square " + str(square))
            return False
    return True

def _forward_check(board: list[list[int]], square: int, value: int) -> bool:
    """Goes through all neighbors of square and eliminates value from their domains. If any domain becomes empty, then this value assignment won't work"""
    board_copy = list(board)
    for neighbor in _get_neighbors(square):

        # Keeps the algorithm from immediately failing
        if neighbor == square:
            continue

        # if the assigned value is in the domain of any neighbor, remove it ***this is the core of forward checking***
        if value in board_copy[neighbor]: board_copy[neighbor].remove(value)

        # make sure board is consistent
        if len(board_copy[neighbor]) == 1:
            if not _is_consistent(board_copy, neighbor, board_copy[neighbor][0]):
                return False
    
        # If the domain of any square is empty, then this value assignment cannot work
        if len(board_copy[neighbor]) == 0:
            return False
    
    # If all checks pass, then this value might work
    board = list(board_copy)
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