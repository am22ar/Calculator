import tkinter

from tkinter import messagebox

root=tkinter.Tk()
root.title("label ex 3")
root.geometry("500x500")

def hello():
    messagebox.showinfo("submit", "submit is clicked")

def hello1():
    messagebox.showinfo("insert", "insert is clicked")

btn=tkinter.Button(root, text="submit", bg="red", command=hello)
btn1=tkinter.Button(root, text="insert", bg="lightblue", command=hello1)

btn.pack()
btn1.pack()

root.mainloop()