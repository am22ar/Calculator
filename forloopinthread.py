from threading import *


def display():
    for i in range(5):
        print("\nchild thread")


t=Thread(target=display)
t.start()

for i in range(5):
    print("\nmain thread")
