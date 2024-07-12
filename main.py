import sys

from backtrack import backtrack_solver, print_board
from csvs import read_csv

if __name__ == "__main__":
    """handles inputting a board and outputting a representation of that board solved"""
    path: str = sys.argv[1]
    verbose = False
    if len(sys.argv) >= 3:
        verbose = bool(sys.argv[2])
    board: list[list[int]] = read_csv(path)
    print("The board to solve:")
    print_board(board)
    print("\n")
    solved_board: list[list[int]] = backtrack_solver(board, verbose)
    if solved_board == None: 
        print("Failed to solve the board")
    else:
        print("The solved board:")
        print_board(solved_board)