from Environment import *
from Environment import _blk

def left(i): return i

def right(i): return (i + 1) % 5

def get_forks(i, leftie: bool): 
    #footman.wait()
    if leftie:
      fork[left(i)].wait()
      fork[right(i)].wait()
    else:
      fork[right(i)].wait() 
      fork[left(i)].wait()

def put_forks(i, leftie): 
    fork[right(i)].signal() 
    fork[left(i)].signal()
    #footman.signal()

def phil0():
    while True:
        get_forks(0, True)
        # eat
        put_forks(0, True)
        # think
        
def phil1():
    while True:
        get_forks(1, False)
        # eat
        put_forks(1, False)
        # think

def phil2():
    while True:
        get_forks(2, False)
        # eat
        put_forks(2, False)
        # think

def phil3():
    while True:
        get_forks(3, False)
        # eat
        put_forks(3, False)
        # think

def phil4():
    while True:
        get_forks(4, False)
        # eat
        put_forks(4, False)
        # think

n = 5
fork = [MySemaphore(1, "semaphore") for i in range(5)]
#footman = MySemaphore(4, "footman")

def setup():
    subscribe_thread(phil0)
    subscribe_thread(phil1)
    subscribe_thread(phil2)
    subscribe_thread(phil3)
    subscribe_thread(phil4)