from Environment import *
from Environment import _blk

aArrived = MySemaphore(3, "semafoor")
bArrived = MySemaphore(3, "semafoor")
cArrived = MySemaphore(3, "semafoor")

def threadA():
    while True:
        print("At the beginning of thread A")  
        aArrived.wait()
        bArrived.wait() 
        cArrived.wait() 
        print("A critical section")
        aArrived.signal() 
        bArrived.signal() 
        cArrived.signal() 
        print("At the end of thread A") 

def threadB():
    while True:
        print("At the beginning of thread B") 
        aArrived.wait() 
        bArrived.wait()
        cArrived.wait() 
        print("B critical section")
        aArrived.signal() 
        bArrived.signal() 
        cArrived.signal() 
        print("At the end of thread B")

def threadC():
    while True:
        print("At the beginning of thread C") 
        aArrived.wait() 
        bArrived.wait() 
        cArrived.wait()
        print("C critical section")
        aArrived.signal() 
        bArrived.signal() 
        cArrived.signal() 
        print("At the end of thread C")

def setup():
    subscribe_thread(threadA)
    subscribe_thread(threadB)
    subscribe_thread(threadC)