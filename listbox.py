from  tkinter import *
from tkinter import messagebox
root=Tk()
root.title("listbox")
root.geometry("400x400")

lbl=Label(root, text="friends: ")
listb=Listbox(root)

listb.insert(1,'akki')
listb.insert(2,'choti')
listb.insert(3,'anya')
listb.insert(4,'myself')

def select():
    item=listb.selection_get()
    messagebox.showinfo("listbox",item)

lbl.pack()
listb.pack()
btn=Button(root, text="submit", command=select)
btn.pack()
root.mainloop()