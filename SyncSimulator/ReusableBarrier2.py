from Environment import *
from Environment import _blk

NUM_THREADS = 4 # The number of threads is known at compile time

# Semaphores for the barrier
mutex = MySemaphore(1, "Mutex")
barrier = MySemaphore(0, "Barrier")

# Shared state for the barrier
counter = 0 # Counts the number of threads that have reached the barrier

def barrier_wait():
    # Protect the shared state using the mutex semaphore
    mutex.wait()

    # Increment the counter and check if this is the last thread to reach the barrier
    if counter == NUM_THREADS - 1:
        # Signal the barrier semaphore to release all threads
        barrier.signal()
        # Reset the counter
        counter = 0
    else:
        # Increment the counter
        counter += 1

    # Release the mutex semaphore
    mutex.signal()

    # Wait for the barrier semaphore to be signaled
    barrier.wait()
