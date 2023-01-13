from Environment import *
from Environment import _blk


N = 4
def threadBaboon(me, other):
    while True:
        mutex.wait()
        capacity.wait()

        if state.v != "EMPTY" or state.v == other.state:
            mutex.signal()
            me.sem.wait()

        state.v = me.state
        me.count.v += 1

        mutex.signal()

        #cs

        mutex.wait()

        me.count.v -= 1

        if me.count.v == 0:
            if me.candidates.v > other.candidates.v:
                me.sem.signal()
            else:
                other.sem.signal()
        
        mutex.signal()



class Baboon(object):
    def __init__(self, count, candidates, sem, state):
        self.count = count
        self.candidates = candidates
        self.sem = sem
        self.state = state

state = MyString("EMPTY", "state")
mutex = MyMutex("mutex")
capacity = MySemaphore(5, "capacity")

northCount = MyInt(0, "nCount")
northCandidates = MyInt(0, "nCand")
northSem = MySemaphore(0, "nSem")

southCount = MyInt(0, "sCount")
southCandidates = MyInt(0, "sCand")
southSem = MySemaphore(0, "sSem")

north_baboon = Baboon (northCount, northCandidates, northSem, "NORTH")
south_baboon = Baboon (southCount, southCandidates, southSem, "SOUTH")

def setup():
    for i in range(N):
        subscribe_thread(lambda: threadBaboon(north_baboon, south_baboon))
    for i in range(N):
        subscribe_thread(lambda: threadBaboon(south_baboon, north_baboon))
