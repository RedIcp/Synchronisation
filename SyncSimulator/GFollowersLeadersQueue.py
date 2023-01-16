from Environment import *
from Environment import _blk

lPipette = MySemaphore(1, "Leader")
fPipette = MySemaphore(1, "Follower")

leader = MySemaphore(0, "LeaderSem")
follower = MySemaphore(0, "FollowerSem")

def threadLeader():
    while True:
        lPipette.wait()

        leader.signal()
        follower.wait()

        lPipette.signal()


def threadFollower():
    while True:
        fPipette.wait()

        follower.signal()
        leader.wait()

        fPipette.signal()

def setup():
    subscribe_thread(threadLeader)
    subscribe_thread(threadFollower)
