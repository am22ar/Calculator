from tkinter import *

root = Tk()

root.title("Container/ Frame")
root.geometry("500x500")

fr = Frame(root, bg="green", bd=5, width=100, height=100, cursor="target").pack(side=BOTTOM)

root.mainloop()

