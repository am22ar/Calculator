from tkinter import *

root= Tk()

root.title("frame example")

root.geometry("400x400")

fr1= Frame(root, bg="light blue", height=200, width=200).grid(padx=100, pady=100)

root.mainloop()