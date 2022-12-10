from Environment import *
from Environment import _blk

# not using turnstile wait

def threadReusableBarrier1():
    global count

    while True:
        mutex.wait() 
        count.v += 1

        if count.v == n: 
            turnstile2.wait()  # lock the second 
            turnstile1.signal() # unlock the first
            
        mutex.signal()

        turnstile1.wait() # first turnstile
        turnstile1.signal()

        print("critical point")# critical point

        mutex.wait() 
        count.v -= 1

        if count.v == 0: 
            turnstile1.wait() # lock the first
            turnstile2.signal()  # unlock the second
            
        mutex.signal()

        turnstile2.wait() # second turnstile
        turnstile2.signal()

n = 3
mutex = MyMutex("mutex")
turnstile1 = MySemaphore(0, "semafoor")
turnstile2 = MySemaphore(1, "semafoor")
# allArrived = MySemaphore(n, "semafoor")
count = MyInt(0, "Number of threads")

def setup():
    for i in range(n):
        subscribe_thread(threadReusableBarrier1)