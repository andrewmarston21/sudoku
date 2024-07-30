from tkinter import Tk, PhotoImage, Label, IntVar, Frame, Entry, ttk
from backtrack import backtrack_solver
from csvs import *


def draw(board: list[list[int]], elapsed_time: float):
    window = Tk()
    window.title("Sudoku")
    window.geometry("700x800+50+50")

    board_img = PhotoImage(file="sudoku_grid.png")
    Label(window, image=board_img).place(relx=0, rely=0)

    labels: list[Label] = []
    for i in range(81):
        labels.append(Label(window, text="0", font=("Arial", 25)))

    idx = 0
    for square in board:
        if len(square) == 1:
            labels[idx] = Label(window, text=str(square[0]), font=("Arial", 25))
        idx += 1

    idx = 0
    for i in range(9):
        for j in range(9):
            labels[idx].place(y=70 * i + 50, x=70 * j + 60)
            idx += 1

    elapsed_time = Label(window, text="The program took " + str(elapsed_time) + " seconds to run", font=("Arial", 13))
    elapsed_time.place(x=10, y=750)

    window.mainloop()


def run_algorithm():
    path = entry.get()
    board_to_solve: list[list[int]] = read_csv(path)
    result: list[list[int]] = backtrack_solver(board_to_solve)

    labels: list[Label] = []
    for i in range(81):
        labels.append(Label(window, text="0", font=("Arial", 25)))

    idx = 0
    for square in result:
        if len(square) == 1:
            labels[idx] = Label(window, text=str(square[0]), font=("Arial", 25))
        idx += 1

    idx = 0
    for i in range(9):
        for j in range(9):
            labels[idx].place(y=70 * i + 50, x=70 * j + 60)
            idx += 1

    button.destroy()


# ENTRY POINT OF PROGRAM
window = Tk()
window.title("Sudoku")
window.geometry("700x800+50+50")

board_img = PhotoImage(file="sudoku_grid.png")
Label(window, image=board_img).place(relx=0, rely=0)

Label(window, text="Path of board:").place(x=10, y=750)

entry = ttk.Entry(window, width=25)
entry.place(x=115, y=750)

button = ttk.Button(window, text="Run", command=run_algorithm)
button.place(x=400, y=750)

window.mainloop()


