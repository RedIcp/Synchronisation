from Environment import *
from Environment import _blk

def left(i): return i

def right(i): return (i + 1) % 5

def get_forks(i): 
    footman.wait()
    fork[right(i)].wait() 
    fork[left(i)].wait()

def put_forks(i): 
    fork[right(i)].signal() 
    fork[left(i)].signal()
    footman.signal()

def phil0():
    while True:
        get_forks(0)
        # eat
        put_forks(0)
        # think
n = 5
fork = [MySemaphore(1) for i in range(5)]
footman = MySemaphore(4, "footman")

def setup():
    subscribe_thread(phil0)

   