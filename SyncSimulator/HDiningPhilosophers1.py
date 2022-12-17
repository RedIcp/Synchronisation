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
        print("0 eating")
        put_forks(0, True)
        print("0 thinking")
        
def phil1():
    while True:
        get_forks(1, False)
        print("1 eating")
        put_forks(1, False)
        print("1 thinking")

def phil2():
    while True:
        get_forks(2, False)
        print("2 eating")
        put_forks(2, False)
        print("2 thinking")

def phil3():
    while True:
        get_forks(3, False)
        print("3 eating")
        put_forks(3, False)
        print("3 thinking")

def phil4():
    while True:
        get_forks(4, False)
        print("4 eating")
        put_forks(4, False)
        print("4 thinking")

n = 5
fork = [MySemaphore(1, "semaphore") for i in range(5)]
#footman = MySemaphore(4, "footman")

def setup():
    subscribe_thread(phil0)
    subscribe_thread(phil1)
    subscribe_thread(phil2)
    subscribe_thread(phil3)
    subscribe_thread(phil4)