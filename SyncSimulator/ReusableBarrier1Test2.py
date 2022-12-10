from Environment import *
from Environment import _blk

NUM_THREADS = 4

mutex = MySemaphore(1, "Mutex")
barrier = MySemaphore(0, "Barrier")

last_thread_to_reach_barrier = False

def threadReusableBarrier1():
    while True:

        global last_thread_to_reach_barrier

        mutex.wait()

        if last_thread_to_reach_barrier:

            barrier.signal()

            last_thread_to_reach_barrier = False

        else:

            last_thread_to_reach_barrier = True

        mutex.signal()

        barrier.wait()

def setup():
    for i in range(NUM_THREADS):
        subscribe_thread(threadReusableBarrier1)