from tkinter import *

root=Tk()

txt=Text(root)

txt.insert(INSERT,"hello")
txt.insert(END, "bye bye")

txt.pack()

txt.tag_add("start","1.0","1.4")
txt.tag_add("end","1.8","1.12")
txt.tag_config("start", background="yellow", foreground="blue")
txt.tag_config("end", background="green", foreground="white")

root.mainloop()