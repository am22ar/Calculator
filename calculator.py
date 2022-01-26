import tkinter
from tkinter import messagebox
root=tkinter.Tk()
root.title("simple calc1")
num1=tkinter.StringVar()
num2=tkinter.StringVar()
result=tkinter.StringVar()
def add():
    n1=num1.get()
    n2=num2.get()
    result=int(n1)+int(n2)
    messagebox.showinfo("addition: ",result)
def sub():
    n1=num1.get()
    n2=num2.get()
    result=int(n1)-int(n2)
    messagebox.showinfo("subtraction: ",result)
def mul():
    n1=num1.get()
    n2=num2.get()
    result=int(n1)*int(n2)
    messagebox.showinfo("multiplication: ",result)
def div():
    n1=num1.get()
    n2=num2.get()
    result=int(n1)/int(n2)
    messagebox.showinfo("division: ",result)
num1_lbl=tkinter.Label(root, text="value1: ").grid(row=0, column=0)
ent1=tkinter.Entry(root, textvariable=num1).grid(row=0, column=1)
num2_lbl=tkinter.Label(root, text="value2: ").grid(row=1, column=0)
ent2=tkinter.Entry(root, textvariable=num2).grid(row=1, column=1)
btn_add=tkinter.Button(root, text="addition: ",command=add).grid(row=2, column=1)
btn_sub=tkinter.Button(root, text="subtraction: ", command=sub).grid(row=2, column=3)
btn_mul=tkinter.Button(root, text="multiplication: ",command=mul).grid(row=2, column=4)
btn_div=tkinter.Button(root, text="division: ",command=mul).grid(row=2, column=6)
result_lbl=tkinter.Label(root,text="result").grid(row=4, column=1)
root.mainloop()

