# What is this?
___

This is a Python implementation of a backtracking seach-based Sudoku-solving algorithm. It takes CSV files as inputs and prints out the solved board.

# How do I use this?
___

Run `main.py` from the command line with the path of the board you want to solve as the first command line argument after the name of the program. Make sure to include `csvs/` at the start of the board's path name.\
If you have a board you'd like the algorithm to solve, use one of the included boards as a reference. (`0` in the board file represents an empty square on a visual Sudoku board.)\
To reduce the verbosity of the output while the algorithm is running, change `verbosity=true` to `verbosity=false` in main.py.
