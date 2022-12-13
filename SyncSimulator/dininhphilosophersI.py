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
    
forks = [Semaphore(1) for i in range(5)]
footman = MySemaphore(4, "footman")

n = 5

def setup():
    for i in range(n):
        subscribe_thread(get_forks)
        subscribe_thread(put_forks)