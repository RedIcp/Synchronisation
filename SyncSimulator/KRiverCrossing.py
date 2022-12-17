from Environment import *
from Environment import _blk

hackers = 0
serfs = 0
hackerQueue = MySemaphore(0, "Hacker")
serfQueue = MySemaphore(0, "Serf")
mutex = MySemaphore(1, "Mutex")

def hackerThread():
    while True:
        global hackers
        global serfs

        mutex.wait()
        
        hackers += 1
        if hackers == 2 and serfs >= 2:
            hackers = 0
            serfs -= 2
            hackerQueue.signal(2)
            print("2 hackers in boat")
        elif hackers == 4:
            hackers = 0
            hackerQueue.signal(4)
            print("4 hackers in boat")
        else:
            mutex.signal()
            hackerQueue.wait()
            
        mutex.signal()


def serfThread():
    while True:
        global hackers
        global serfs
        
        mutex.wait()

        serfs += 1
        if serfs == 2 and hackers >= 2:
            serfs = 0
            hackers -= 2
            serfQueue.signal(2)
        elif serfs == 4:
            serfs = 0
            serfQueue.signal(4)
        else:
            mutex.signal()
            serfQueue.wait()
            
        mutex.signal()

def setup():
    for i in range(7):
        subscribe_thread(hackerThread)
        subscribe_thread(serfThread)