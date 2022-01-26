from tkinter import *

root = Tk()

root.title("Container/ Frame")
root.geometry("500x500")

fr1 = Frame(root, bg="light blue", bd=5, width=40, height=30, cursor="target").pack(side=TOP)

fr2 = Frame(root, bg="purple", bd=5, width=20, height=30, cursor="target").pack(side=LEFT)

fr3 = Frame(root, bg="brown", bd=5, width=40, height=30, cursor="target").pack(side=RIGHT)

fr4 = Frame(root, bg="yellow", bd=5, width=40, height=30, cursor="target").pack(side=BOTTOM)
root.mainloop()

