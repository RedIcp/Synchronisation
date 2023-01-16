from Environment import *
from Environment import _blk

barrier = MySemaphore(0, "Barrier")

aReached = MySemaphore(0, "Barrier")
bReached = MySemaphore(0, "Barrier")
cReached = MySemaphore(0, "Barrier")
dReached = MySemaphore(0, "Barrier")


def threadA():
    while True:
        aReached.signal(3)
        bReached.wait()
        cReached.wait()
        dReached.wait()

def threadB():
    while True:
        bReached.signal(3)
        aReached.wait()
        cReached.wait()
        dReached.wait()

def threadC():
    while True:
        cReached.signal(3)
        bReached.wait()
        aReached.wait()
        dReached.wait()

def threadD():
    while True:
        bReached.wait()
        cReached.wait()
        aReached.wait()
        dReached.signal(3)       
        




def setup():
    subscribe_thread(threadA)
    subscribe_thread(threadB)
    subscribe_thread(threadC)
    subscribe_thread(threadD)