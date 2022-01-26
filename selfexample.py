from threading import *

class demo:

    def display(self):
        for i in range(5):
            print("child thread\n")

obj=demo()
t=Thread(target=obj.display)
t.start()

for i in range(5):
    print("main thread")
