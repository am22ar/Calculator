from threading import *

def m():

    print("child thread\n")

t=Thread(target=m)

t.start()

print("main thread identification number:" , current_thread().ident)

print("child thread identification number:" , t.ident)
