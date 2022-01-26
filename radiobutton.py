from  tkinter import *
from tkinter import messagebox
root=Tk()
root.title("radio button")

var=StringVar()
def sel_RB():
    val=var.get()
    str="vaccination status: "+val
    lbl.config(text=str)


r1=Radiobutton(root, text="fully vaccinated", variable=var, value="fully vaccinated", command=sel_RB)
r1.pack()

r2=Radiobutton(root, text="partially vaccinated", variable=var, value="partially vaccinated", command=sel_RB)
r2.pack()

r3=Radiobutton(root, text="not vaccinated", variable=var, value="not vaccinated", command=sel_RB)
r3.pack()

lbl=Label(root)
lbl.pack()

root.mainloop()