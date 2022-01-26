from threading import *
import time
l=RLock()
def fact(n):
    l.acquire()
    if n==0:
        result=1
    else:
        result=n*fact(n-1)
    l.release()
    return result
def results(n):
    print("\nfactorial of ",n,"is",fact(n))
    #print("\nfact is",fact(n))
t1 = Thread(target=results , args=(5,))
t2 = Thread(target=results , args=(3,))
t1.start()
t2.start()
