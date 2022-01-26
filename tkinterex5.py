import tkinter
from tkinter import *

root= tkinter.Tk()

root.title(" canvas example")

root.geometry("600x600")

can= tkinter.Canvas(root, bg="yellow", height=290, width=280)

coord= 10, 50, 240, 210

arc= can.create_arc(coord, start=0, extent=300, fill="red")

can.pack()

root.mainloop()