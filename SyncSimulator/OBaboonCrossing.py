from Environment import *
from Environment import _blk


state = MyString("EMPTY", "state") # other states: “NORTH”, “SOUTH”
mutex = MyMutex("mutex")
capacity = MySemaphore(5, "capacity")


northCount = MyInt(0, "nCount")
northCandidates = MyInt(0, "nCand")
# northSem acts like a ‘queue’, where either you open it for yourself, 
# or it is opened by the south baboon (when he leaves)
northSem = MySemaphore(0, "nSem")


southCount = MyInt(0, "sCount")
southCandidates = MyInt(0, "sCand")
southSem = MySemaphore(0, "sSem")

def threadBaboon():
    