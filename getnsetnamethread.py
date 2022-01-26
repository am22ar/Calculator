from threading import *

print("Main thread name:",current_thread().getName())

current_thread().setName("MyThread")

print("after customization of thread:",current_thread().getName())
