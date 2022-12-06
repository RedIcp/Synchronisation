from Environment import *
from Environment import _blk

n = 3

mutex = MySemaphore(1, "semafoor")
turnstile1 = MySemaphore(0, "semafoor")
turnstile2 = MySemaphore(1, "semafoor")
allArrived = MySemaphore(n, "semafoor")

count = 0

def threadReusableBarrier1():
    global count

    while True:
        mutex.wait() 
        count += 1

        if count == n: 
            turnstile2.wait()  # lock the second 
            turnstile1.signal() # unlock the first
            
        mutex.signal()

        turnstile1.wait() # first turnstile
        turnstile1.signal()

        print("critical point")# critical point

        mutex.wait() 
        count -= 1

        if count == 0: 
            turnstile1.wait() # lock the first
            turnstile2.signal()  # unlock the second
            
        mutex.signal()

        turnstile2.wait() # second turnstile
        turnstile2.signal()


def setup():
    for i in range(n):
        subscribe_thread(threadReusableBarrier1)