from Environment import *
from Environment import _blk


N = 4
def threadBaboon(me, other):
    while True:
        mutex.wait()

        if state.v == other.state or (state.v != "EMPTY" and other.candidates.v > 0):
            me.candidates.v += 1
            mutex.signal()
            me.sem.wait()
            me.count.v += 1
            if me.count.v == 1:
                state.v = me.state
        else:
            me.count.v += 1
            if me.count.v == 1:
                state.v = me.state
            mutex.signal()
            capacity.wait()

        print(state.v + " is crossing")

        mutex.wait()

        me.count.v -= 1

        if me.count.v == 0:
            state.v = "EMPTY"
            if other.candidates.v > 0:
                other.sem.signal()
                other.candidates.v -= 1
            elif me.candidates.v > 0:
                other.sem.signal()
                other.candidates.v -= 0
        
        mutex.signal()

        capacity.signal()



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
