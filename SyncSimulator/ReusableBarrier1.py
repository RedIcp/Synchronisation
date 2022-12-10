from Environment import *
from Environment import _blk

mutex = MySemaphore(1, "Mutex")

barrier = MySemaphore(0, "Barrier")

aReachedBarrier = False
bReachedBarrier = False
cReachedBarrier = False
dReachedBarrier = False


def threadA():
    while True:
        global aReachedBarrier
        global bReachedBarrier
        global cReachedBarrier
        global dReachedBarrier

        mutex.wait()
        if bReachedBarrier & cReachedBarrier & dReachedBarrier:
            aReachedBarrier = True
            mutex.signal()
            print("A is in the barrier")
            barrier.signal()
        else:
            aReachedBarrier = True
            mutex.signal()
            print("A is in the barrier")
            barrier.wait()

        barrier.signal()

        aReachedBarrier = False
        bReachedBarrier = False
        cReachedBarrier = False
        dReachedBarrier = False

        print("A got out of barrier")

def threadB():
    while True:
        global aReachedBarrier
        global bReachedBarrier
        global cReachedBarrier
        global dReachedBarrier

        mutex.wait()
        if aReachedBarrier & cReachedBarrier & dReachedBarrier:
            bReachedBarrier = True
            mutex.signal()
            print("B is in the barrier")
            barrier.signal()
        else:
            bReachedBarrier = True
            mutex.signal()
            print("B is in the barrier")
            barrier.wait()

        barrier.signal()

        aReachedBarrier = False
        bReachedBarrier = False
        cReachedBarrier = False
        dReachedBarrier = False

        print("B got out of barrier")


def threadC():
    while True:
        global aReachedBarrier
        global bReachedBarrier
        global cReachedBarrier
        global dReachedBarrier

        mutex.wait()
        if bReachedBarrier & aReachedBarrier & dReachedBarrier:
            cReachedBarrier = True
            mutex.signal()
            print("C is in the barrier")
            barrier.signal()
        else:
            cReachedBarrier = True
            mutex.signal()
            print("C is in the barrier")
            barrier.wait()

        barrier.signal()

        aReachedBarrier = False
        bReachedBarrier = False
        cReachedBarrier = False
        dReachedBarrier = False

        print("C got out of barrier")


def threadD():
    while True:
        global aReachedBarrier
        global bReachedBarrier
        global cReachedBarrier
        global dReachedBarrier

        mutex.wait()
        if bReachedBarrier & cReachedBarrier & aReachedBarrier:
            dReachedBarrier = True
            mutex.signal()
            print("D is in the barrier")
            barrier.signal()
        else:
            dReachedBarrier = True
            mutex.signal()
            print("D is in the barrier")
            barrier.wait()

        barrier.signal()

        aReachedBarrier = False
        bReachedBarrier = False
        cReachedBarrier = False
        dReachedBarrier = False

        print("D got out of barrier")

def setup():
    subscribe_thread(threadA)
    subscribe_thread(threadB)
    subscribe_thread(threadC)
    subscribe_thread(threadD)