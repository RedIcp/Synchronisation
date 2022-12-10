from Environment import *
from Environment import _blk

mutex = MySemaphore(1, "Mutex")

leaderQueue = MySemaphore(0, "Leader")
followerQueue = MySemaphore(0, "Follower")

isThereFollower = False
isThereLeader = False

def threadLeader():
    while True:

        global isThereFollower
        global isThereLeader

        mutex.wait()

        if isThereFollower:

            isThereFollower = False
            
            followerQueue.signal()

        else:

            isThereLeader = True

            mutex.signal()

        leaderQueue.wait()

        mutex.signal()


def threadFollower():
    while True:
        
        global isThereFollower
        global isThereLeader
        
        mutex.wait()

        if isThereLeader:

            isThereLeader = False
            
            leaderQueue.signal()

        else:

            isThereFollower = True

            mutex.signal()

        followerQueue.wait()

def setup():
    subscribe_thread(threadLeader)
    subscribe_thread(threadFollower)
