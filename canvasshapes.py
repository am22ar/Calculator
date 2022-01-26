import tkinter

root= tkinter.Tk()

root.title("canvas example")

root.geometry("600x600")

can=tkinter.Canvas(root, bg="blue", height=600, width=600)

rect1=can.create_rectangle(30,10,120,80, fill="yellow", outline="brown")

rect2=can.create_rectangle(150,10,240,80, fill="light green", outline="white")

rect3=can.create_rectangle(270,10,370,80, fill="red", outline="green", width=4)

rect4=can.create_rectangle(500,10,400,80, fill="orange", outline="brown")

ovl1=can.create_oval(15,180,120,200, fill="red" , outline="yellow", width=10)

ovl2=can.create_oval(100,80,200,160, fill="red" , outline="yellow", width=10)

can.pack()

can.mainloop()