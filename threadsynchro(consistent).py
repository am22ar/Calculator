from threading import *

import time

def wish(name,age):

    for i in range(3):

        print("\nHI",name)

        time.sleep(2)

        print("\nyour age is",age)


t1=Thread(target=wish,args=("amar",21))

t2=Thread(target=wish,args=("patil",20))


t1.start()

t2.start()
