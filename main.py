import sys
from time import time

from backtrack import backtrack_solver, print_board
from csvs import read_csv

if __name__ == "__main__":
    """handles inputting a board and outputting a representation of that board solved"""
    path: str = sys.argv[1]
    verbosity = False
    board: list[list[int]] = read_csv(path)
    print("The board to solve:")
    print_board(board)
    print("\n")
    print("This may take several minutes:")
    start_time = time()
    solved_board: list[list[int]] = backtrack_solver(board, verbose=verbosity)
    end_time = time()
    elapsed_time = round(end_time - start_time, 2)
    if solved_board is None:
        print("Failed to solve the board")
    else:
        print("The solved board:")
        print_board(solved_board)
    print("The program took " + str(elapsed_time) + " seconds to run")
