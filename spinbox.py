from tkinter import *

root=Tk()
root.title("spinbox example")
root.geometry("400x400")

cur_val=StringVar()

def val_sel():
    print(cur_val.get())

spin=Spinbox(root,from_=0 , to=10, values=(1,3,5,7,9), textvariable = cur_val, command = val_sel)

spin.pack()

root.mainloop()