import tkinter
from tkinter import *

root=tkinter.Tk()
root.title("checkbox example")
root.geometry("400x400")

checkvar1 = IntVar()
checkvar2 = IntVar()

c1=Checkbutton(root, text="marathi", variable=checkvar1, onvalue=1, offvalue=0, height=2)

c2=Checkbutton(root, text="english", variable=checkvar2, onvalue=1, offvalue=0, height=2)

c3=Checkbutton(root, text="hindi", onvalue=1, offvalue=0, height=2)

c4=Checkbutton(root, text="kannada", onvalue=1, offvalue=0, height=2)

c1.pack()
c2.pack()
c3.pack()
c4.pack()

root.mainloop()
