from tkinter import *

root=Tk()
root.title("simple calc2")

num1=StringVar()

num2=StringVar()

result=StringVar()


def add():
    n1=num1.get()
    n2=num2.get()
    result=int(n1)+int(n2)
    strresult="addition is: "+str(result)
    result_lbl.config(text=strresult)

def sub():
    n1=num1.get()
    n2=num2.get()
    result=int(n1)-int(n2)
    strresult="subtraction is"+ str(result)
    result_lbl.config(text=strresult)


def mul():
    n1=num1.get()
    n2=num2.get()
    result=int(n1)*int(n2)
    strresult = "multiplication is: "+str(result)
    result_lbl.config(text=strresult)


def div():
    n1=num1.get()
    n2=num2.get()
    result=int(n1)/int(n2)
    strresult = "division is: "+str(result)
    result_lbl.config(text=strresult)

num1_lbl=Label(root, text="value1: ").grid(row=0, column=0)
ent1=Entry(root, textvariable=num1).grid(row=0, column=1)

num2_lbl=Label(root, text="value2: ").grid(row=1, column=0)
ent2=Entry(root, textvariable=num2).grid(row=1, column=1)

btn_add=Button(root, text="addition: ",command=add).grid(row=2, column=1)

btn_sub=Button(root, text="subtraction: ", command=sub).grid(row=2, column=3)

btn_mul=Button(root, text="multiplication: ",command=mul).grid(row=2, column=4)

btn_div=Button(root, text="division: ",command=mul).grid(row=2, column=6)


result_lbl=Label(root,text="result")
result_lbl.grid(row=3)

root.mainloop()

