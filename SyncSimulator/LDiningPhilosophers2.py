from Environment import *
from Environment import _blk

def phil(i):
    while True:
        mu.wait()
        
        while (not forkA[leftFork(i)].v) or (not forkA[right(i)].v):
            print("Philosopher: " + str(i) + " waiting...")
            cvphil[i].wait()
            
        print("Philosopher: " + str(i) + " getting forks.")
        forkA[leftFork(i)].v = False
        forkA[right(i)].v = False
        
        mu.signal()
        _blk() # CS
        print("Philosopher: " + str(i) + " eating!")
        mu.wait()
        
        forkA[leftFork(i)].v = True
        forkA[right(i)].v = True
        print("Philosopher: " + str(i) + " putting forks.")
        
        if forkA[left(i)].v:
            cvphil[left(i)].notify()
            print("P: " + str(i) + " signaling P: " + str(left(i)))
            
        if forkA[rightRightFork(i)].v:
            cvphil[right(i)].notify()
            print("P: " + str(i) + " signaling P: " + str(right(i)))
            
        print("Philosopher: " + str(i) + " thinking.")
        mu.signal()

def leftFork(i): return i

# left neighbor or left left fork
def left(i):
    if i == 4:
        return 0
    else:
        return i + 1

# right fork or right neighbor
def right(i):
    if i == 0:
        return 4
    else:
        return i - 1
    
def rightRightFork(i): 
    if i == 0:
        return 3
    elif i == 1:
        return 4
    else:
        return i - 2

n = 5
mu = MyMutex("mutex")
forkA = [MyBool(True, "forkAvailable") for i in range(n)]
cvphil = [MyConditionVariable(mu, "cvphil") for i in range(n)]

def setup():
    subscribe_thread(lambda: phil(0))
    subscribe_thread(lambda: phil(1))
    subscribe_thread(lambda: phil(2))
    subscribe_thread(lambda: phil(3))
    subscribe_thread(lambda: phil(4))