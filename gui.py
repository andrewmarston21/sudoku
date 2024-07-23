from tkinter import Tk, PhotoImage, Label, IntVar
window = Tk()
window.title("Sudoku")
window.minsize(700, 700)
window.maxsize(700, 700)
window.geometry("700x700+50+50")

board_img = PhotoImage(file="sudoku_grid.png")
img = Label(window, image=board_img)
img.pack()

window.mainloop()
