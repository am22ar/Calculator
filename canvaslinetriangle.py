import tkinter

root=tkinter.Tk()

root.title("canvas line example")

root.geometry("500x500")

can=tkinter.Canvas(root,bg="red", height=400, width=400)

ln=can.create_line(15, 25, 208, 25, dash=(4,2))

ln1=can.create_line(160, 58, 408, 50)

tri=can.create_line(55, 85, 155, 85, 185, 180, 55, 85)

can.pack()

root.mainloop()