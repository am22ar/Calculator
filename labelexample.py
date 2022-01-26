import  tkinter

root=tkinter.Tk()
root.title("label example")
root.geometry("400x400")

def hello():
    print("submit button")


def newone():
    print("insert button")

btn1=tkinter.Button(root, text="submit", bg="red", command=hello)
btn2=tkinter.Button(root, text="insert", bg="lightgreen", command=newone)


btn1.pack()
btn2.pack()


root.mainloop()