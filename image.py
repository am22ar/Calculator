from tkinter import *

root=Tk()

can=Canvas(root,height=1000, width=1000, bg="red")

can.pack()

img=PhotoImage(file="C:\\Users\\Amar\\Goku.png")

can.create_image(20,20, anchor=NW, image=img)

root.mainloop()