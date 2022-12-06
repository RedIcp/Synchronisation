from Environment import *
from Environment import _blk

aArrived = MySemaphore(0, "semafoor")
bArrived = MySemaphore(0, "semafoor")
cArrived = MySemaphore(0, "semafoor")
dArrived = MySemaphore(0, "semafoor")

a1Arrived = MySemaphore(0, "semafoor")
b1Arrived = MySemaphore(0, "semafoor")
c1Arrived = MySemaphore(0, "semafoor")
d1Arrived = MySemaphore(1, "semafoor")

def threadA():
    while True:
        d1Arrived.wait()
        print("1")
        aArrived.signal() 
        dArrived.wait()
        print("5")
        a1Arrived.signal()

def threadB():
    while True:
        aArrived.wait()
        print("2")
        bArrived.signal()
        a1Arrived.wait()
        print("6")
        b1Arrived.signal()


def threadC():
    while True: 
        bArrived.wait() 
        print("3")
        cArrived.signal()
        b1Arrived.wait()
        print("7")
        c1Arrived.signal()


def threadD():
    while True: 
        cArrived.wait() 
        print("4")
        dArrived.signal() 
        c1Arrived.wait()
        print("8")


def setup():
    subscribe_thread(threadA)
    subscribe_thread(threadB)
    subscribe_thread(threadC)
    subscribe_thread(threadD)