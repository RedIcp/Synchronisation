from Environment import *
from Environment import _blk

NUM_THREADS = 4 # The number of threads is known at compile time

# Semaphores for the barrier
mutex = MySemaphore(1, "Mutex") # Used to protect the barrier's shared state
barrier = MySemaphore(0, "Barrier") # Used to block threads until they have all reached the barrier

# Shared state for the barrier
last_thread_to_reach_barrier = False # Indicates whether the current thread is the last thread to reach the barrier

def barrier_wait():
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
        subscribe_thread(barrier_wait)