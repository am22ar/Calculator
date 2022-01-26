#import threading

from threading import *


def disp():
    print("child thread\n")


t=Thread(target=disp)

t.start()

print("main thread")
