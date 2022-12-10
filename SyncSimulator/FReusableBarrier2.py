from Environment import *
from Environment import _blk

NUM_THREADS = 4

mutex = MySemaphore(1, "Mutex")
turnstile1 = MySemaphore(0, "Turnstile1")
turnstile2 = MySemaphore(0, "Turnstile2")


counter = 0

def threadReusableBarrier2():
    while True:
        global counter
        global NUM_THREADS

        mutex.wait()

        counter += 1

        if counter == NUM_THREADS:

            turnstile1.signal()

        mutex.signal()

        turnstile1.wait()
        turnstile1.signal()

        mutex.wait()

        counter -= 1

        if counter == 0:

            turnstile2.signal()

        mutex.signal()

        turnstile2.wait()
        turnstile2.signal()


def setup():
    for i in range(NUM_THREADS):
        subscribe_thread(threadReusableBarrier2)