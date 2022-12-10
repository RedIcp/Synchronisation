import threading

# Semaphores for the followers and leaders problem
mutex = threading.Semaphore(1) # Used to protect the shared state
pipet = threading.Semaphore(0) # Used to block threads until they have all reached the critical section

# Shared state for the followers and leaders problem
followers_in_cs = 0 # The number of followers currently in the critical section
leaders_waiting = 0 # The number of leaders waiting to enter the critical section

def follower():
    # Protect the shared state using the mutex semaphore
    mutex.acquire()

    # Increment the number of followers in the critical section
    followers_in_cs += 1

    # Check if all followers are in the critical section
    if followers_in_cs == NUM_FOLLOWERS:
        # Signal the pipet semaphore to release all leaders
        pipet.release()
    else:
        # Release the mutex semaphore
        mutex.release()

    # Wait for the pipet semaphore to be signaled
    pipet.acquire()

    # Protect the shared state using the mutex semaphore
    mutex.acquire()

    # Decrement the number of followers in the critical section
    followers_in_cs -= 1

    # Check if all followers have left the critical section
    if followers_in_cs == 0:
        # Signal the pipet semaphore to release the next batch of followers and leaders
        pipet.release()