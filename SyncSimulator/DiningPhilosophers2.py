from Environment import *
from Environment import _blk

def left(i): return i

def right(i): return (i + 1) % 5

def get_forks(i): 
    fork[right(i)].wait() 
    fork[left(i)].wait()

def put_forks(i): 
    fork[right(i)].signal() 
    fork[left(i)].signal()

def phil0():
    while True:
        mu.wait()
        while not leftForkAvilable[i-1] and not rightForkAvailable[i+1]:
            cvphil0.wait()

        _blk()
        # CS
        get_forks(0, True)
        print("0 eating")
        put_forks(0, True)
        
        cvphil1.notify()
        cvphil4.notify()
        
        print("0 thinking")

        mu.signal()


n = 5
fork = [MySemaphore(1, "semaphore") for i in range(5)]
mu = MyMutex("mutex")
cvphil0 = MyConditionVariable(mu, "cvphil0")
cvphil1 = MyConditionVariable(mu, "cvphil1")
cvphil2 = MyConditionVariable(mu, "cvphil2")
cvphil3 = MyConditionVariable(mu, "cvphil3")
cvphil4 = MyConditionVariable(mu, "cvphil4")


def setup():
    subscribe_thread(phil0)
    subscribe_thread(phil1)
    subscribe_thread(phil2)
    subscribe_thread(phil3)
    subscribe_thread(phil4)