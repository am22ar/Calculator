from tkinter import*
from tkinter import messagebox

root=Tk()

root.title("Menu Deemonstration")

def new_file():
    messagebox.showinfo("file menu....","You have clicked the new file menu...")

def cut():
    rt=Tk()
    rt.title("Cut Window")
    rt.geometry("200x200")
    rt.mainloop()

menubar=Menu(root)

file=Menu(menubar,tearoff=0)
menubar.add_cascade(label="File",menu=file)
file.add_command(label="new file",command=new_file)
file.add_separator()
file.add_command(label="Open...",command=None)
file.add_separator()
file.add_command(label="Save",command=None)
file.add_separator()
file.add_command(label="Exit",command=root.destroy)

edit=Menu(menubar,tearoff=0)
menubar.add_cascade(label="Edit",menu=edit)
edit.add_command(label="Cut",command=cut)
edit.add_command(label="Copy",command=None)
edit.add_command(label="Paste",command=None)
edit.add_separator()
edit.add_command(label="Select All...",command=None)
edit.add_command(label="Find",command=None)
edit.add_command(label="Find Again",command=None)

help_menu=Menu(menubar,tearoff=0)
menubar.add_cascade(label="Help",menu=help_menu)
help_menu.add_command(label="Help",command=None)
help_menu.add_command(label="Tkhelp",command=None)
help_menu.add_separator()
help_menu.add_command(label="About Tk",command=None)
root.config(menu=menubar)
mainloop()