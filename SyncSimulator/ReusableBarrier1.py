from Environment import *
from Environment import _blk

n = 3

mutex = MyMutex("mutex")
turnstile1 = MySemaphore(0, "semafoor")
turnstile2 = MySemaphore(0, "semafoor")
allArrived = MySemaphore(n, "semafoor")

def threadReusableBarrier1():
    while True:
        mutex.wait() 
        count += 1

        if count == n: 
            turnstile2.wait()  # lock the second 
            turnstile.signal() # unlock the first
            
        mutex.signal()

        turnstile.wait() # first turnstile
        turnstile.signal()

        print("critical point")# critical point

        mutex.wait() 
        count -= 1

        if count == 0: 
            turnstile.wait() # lock the first
            turnstile2.signal()  # unlock the second
            
        mutex.signal()

        turnstile2.wait() # second turnstile
        turnstile2.signal()


def setup():
    for i in range(n):
        subscribe_thread(threadReusableBarrier1)