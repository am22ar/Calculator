from tkinter import *

root=Tk()

root.title("label ex 2")
root.geometry("500x500")
var=StringVar()
var1=StringVar()

lb1=Label(root, textvariable=var, relief=RAISED, bg="White")
lb2=Label(root, textvariable=var1, relief=RAISED, bg="yellow")

var.set("lable is the")
var1.set("Submit")

lb1.pack()
lb2.pack()

root.mainloop()
