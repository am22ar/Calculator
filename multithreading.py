from threading import *
import time
def divison(numbers):
    for n in numbers:
      time.sleep(1)
      print("Double:", n/5)
def multiplication(numbers):
    for n in numbers:
      time.sleep(1)
      print("Square:", n*5)
numbers=[10,20,30,40,50]
begintime=time.time()
divison(numbers)
multiplication(numbers)
print("The total time taken:", time.time()-begintime)
