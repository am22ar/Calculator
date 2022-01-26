from tkinter import *

root = Tk()

root.title("frame examples")
root.geometry("400x400")

fr1 = Frame(root, width=100, height=50, highlihghtcolor="yellow", highlightbackground="red",
           highlightthickness=5).pack(side=TOP)

root.mainloop()