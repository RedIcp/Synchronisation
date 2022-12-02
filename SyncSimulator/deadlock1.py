from Environment import *
from Environment import _blk

aArrived = MySemaphore(0, "semafoor")
bArrived = MySemaphore(0, "semafoor")
cArrived = MySemaphore(0, "semafoor")

def threadA():
    while True:
        print("At the beginning of thread A")  
        bArrived.wait() 
        cArrived.wait() 
        aArrived.wait()
        print("A.signal")
        aArrived.signal() 
        print("At the end of thread A") 

def threadB():
    while True:
        print("At the beginning of thread B") 
        aArrived.wait() 
        cArrived.wait() 
        bArrived.wait() 
        print("B.signal")
        bArrived.signal() 
        print("At the end of thread B")

def threadC():
    while True:
        print("At the beginning of thread C") 
        aArrived.wait() 
        bArrived.wait() 
        cArrived.wait() 
        print("C.signal")
        cArrived.signal()
        print("At the end of thread C")

def setup():
    subscribe_thread(threadA)
    subscribe_thread(threadB)
    subscribe_thread(threadC)