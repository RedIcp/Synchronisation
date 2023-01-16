from Environment import *
from Environment import _blk

aArrived = MySemaphore(0, "semafoor")
bArrived = MySemaphore(0, "semafoor")
cArrived = MySemaphore(1, "semafoor")

def threadA():
    while True:
        cArrived.wait()
        print("A critical section")
        aArrived.signal()
        aArrived.signal()

def threadB():
    while True:
        aArrived.wait()
        print("B critical section")
        bArrived.signal()

def threadC():
    while True: 
        bArrived.wait()
        aArrived.wait()
        print("C critical section")
        cArrived.signal() 

def setup():
    subscribe_thread(threadA)
    subscribe_thread(threadB)
    subscribe_thread(threadC)