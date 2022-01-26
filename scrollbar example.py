import tkinter
root=tkinter.Tk()
root.title("Scrollbar Example")
root.geometry("200x100")
scr1=tkinter.Scrollbar(root)
scr1.pack(side="right",fill="y")
scr2=tkinter.Scrollbar(root)
scr2.pack(side="left",fill="y")
root.mainloop()