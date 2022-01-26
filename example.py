import tkinter

root=tkinter.Tk()

root.title("canvas example")

root.geometry("500x500")

can=tkinter.Canvas(root, bg="blue", height=400, width=400)

coord=10 , 50, 240 ,210

arc=can.create_arc(coord, start=0, extent=230, fill="orange")

can.pack()

root.mainloop()