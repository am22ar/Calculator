from threading import *

import time

s=Semaphore(3)
def wish(name,age):
    for i in range(3):
        s.acquire()
        print(name)
        print(age)
        time.sleep(2)
        s.release()
t1=Thread(target=wish,args=("\nx",21))
t2=Thread(target=wish,args=("\na",20))
t3=Thread(target=wish,args=("\nb",22))
t4=Thread(target=wish,args=("\nd",19))
t1.start()
t2.start()
t3.start()
t4.start()
        
