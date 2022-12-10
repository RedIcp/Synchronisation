from Environment import *
from Environment import _blk

NUM_THREADS = 4

mutex = MySemaphore(1, "Mutex")
barrier = MySemaphore(0, "Barrier")

is_last_thread = False

def threadReusableBarrier1():
    while True:

        global is_last_thread

        mutex.wait()

        if is_last_thread:

            barrier.signal()

            is_last_thread = False

        else:

            is_last_thread = True

        mutex.signal()

        barrier.wait()

def setup():
    for i in range(NUM_THREADS):
        subscribe_thread(threadReusableBarrier1)