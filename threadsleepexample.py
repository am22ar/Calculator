from threading import *

import time

def div(num):
    for n in num:
        time.sleep(1)
        print("\ndivision is=",n/2)

def mul(num):
    for n in num:
        time.sleep(1)
        print("\nmultiplication is=",n*2)

num= [120.321, 200, 30, 420]
begtime=time.time()

t1=Thread(target=div,args=[num,])
t2=Thread(target=mul,args=[num,])
t1.start()
t2.start()


t1.join()
t2.join()
#div(num)
#mul(num)

print("the total time taken:",time.time()-begtime)
