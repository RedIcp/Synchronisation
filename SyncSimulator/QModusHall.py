from Environment import *

def threadPerson(me, other):
    while True:
        mutex.wait()
        if state.v == other.state_walk:
            # first Prude arrives while Heathens walking
            state.v = other.state_trans1 
        while not (state.v == "NEUTRAL" or state.v == me.state_walk or state.v == other.state_trans2):
            me.cv.wait()
        state.v = me.state_walk

        me.count.v += 1
        mutex.signal()
        # CS
        mutex.wait()
        me.count.v -= 1
          
        if me.count.v == 0:
            if state.v == me.state_trans1:
                # the last heathens left the path
                state.v = me.state_trans2
                other.cv.notify_all()
            else:
                state.v = "NEUTRAL"
        mutex.signal()


class Person(object):
    def __init__(self, count, cv, state_walk, state_trans1, state_trans2):
        self.count = count
        self.cv = cv
        self.state_walk = state_walk
        self.state_trans1 = state_trans1
        self.state_trans2 = state_trans2

N = 4
state = MyString("NEUTRAL", "state")
mutex = MyMutex("mutex")
heathen = Person (MyInt(0, "heathenCount"),
              MyConditionVariable(mutex, "heathenCV"), "HEATHENS_RULE", "TRANS_TO_PRUDES_1", "TRANS_TO_PRUDES_2")
prude = Person (MyInt(0, "prudeCount"),
               MyConditionVariable(mutex, "prudeCV"), "PRUDES_RULE", "TRANS_TO_HEATHENS_1", "TRANS_TO_HEATHENS_2")

def setup():
    for i in range(N):
        subscribe_thread(lambda: threadPerson(heathen, prude))
    for i in range(N):
        subscribe_thread(lambda: threadPerson(prude, heathen))