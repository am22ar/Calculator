from tkinter import  *
from tkinter import messagebox

root = Tk()

root.title("Registration Form ")
root.geometry("500x500")

def get_val():
    var1=e_fullname.get()
    var2=e_email.get()
    messagebox.showinfo("registration form: ", var1+" "+var2)

lbl_register=Label(root, text="Registration form", width=20, font=("bold",20))

lbl_register.place(x=90 , y=60)

lbl_fullname=Label(root, text="Full name", width=15, font=("bold",10))
lbl_fullname.place(x=80 , y=130)

e_fullname=Entry(root)
e_fullname.place(x=240 , y=130)

lbl_email=Label(root, text="E-Mail", width=15, font=("bold",10))
lbl_email.place(x=68,y=180)

e_email=Entry(root)
e_email.place(x=240 , y=180)

lbl_gender=Label(root, text="Gender", width=15, font=("bold",10))
lbl_gender.place(x=70,y=230)

var=IntVar()

Radiobutton(root,text="Male",padx=5, variable=var, value=1).place(x=235, y=230)
Radiobutton(root,text="Female",padx=20, variable=var, value=2).place(x=298, y=230)

lbl_country=Label(root, text="Country", width=15, font=("bold",10))
lbl_country.place(x=70,y=280)

list_country=['INDIA', 'USA', 'UK', 'GERMANY','SRILANKA']

c=StringVar()

droplist=OptionMenu(root, c, *list_country)
droplist.config(width=20)

c.set("Select your Country")
droplist.place(x=240,y=280)

lbl_lang=Label(root, text="Language", width=15, font=("bold",10))
lbl_lang.place(x=75,y=330)

var_check1=IntVar()
Checkbutton(root, text="english", variable=var_check1).place(x=230, y=330)

var_check2=IntVar()
Checkbutton(root, text="hindi", variable=var_check2).place(x=290, y=330)

var_check1=IntVar()
Checkbutton(root, text="marathi", variable=var_check1).place(x=330, y=330)

Button(root, text="submit", width=20, bg="grey",fg="white", command=get_val).place(x=180,y=380)

root.mainloop()