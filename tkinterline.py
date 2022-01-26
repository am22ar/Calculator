import tkinter

root=tkinter.Tk()

root.title("canvas line example")

root.geometry("500x500")

can=tkinter.Canvas(root,bg="red", height=400, width=400)

ln=can.create_line(15,25,200,25)

ln1=can.create_line(160,58,400,50)

can.pack()

root.mainloop()