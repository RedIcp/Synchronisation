from Environment import *
from Environment import _blk

elves = 0
reindeer = 0
santaSem = MySemaphore(0, "Santa")
reindeerSem = MySemaphore(0, "Rendieer")
elfTex = MySemaphore(0, "Elf")
mutex = MySemaphore(1, "Mutex")

def santaThread():
    while True:
        global reindeer
        global elves

        santaSem.wait()
        mutex.wait()

        if elves >= 3:
            print("help elves")
            ## helping all the waiting elves
            elfTex.signal(elves)
        elif reindeer >= 9:
            print("prepare sleigh")
            reindeerSem.signal(9)
            reindeer -= 9

        mutex.signal()

def reindeersThread():
    while True:
        global reindeer

        mutex.wait()

        reindeer += 1
        if reindeer == 9:
            print("9 reindeers arrived")
            santaSem.signal()

        mutex.signal()
        reindeerSem.wait()

        print("get hitched")

def elvesThread():
    while True:
        global elves
        ## no need of elftex here because now it is allowed for more than 3 elves
        ## to pass through
        mutex.wait()

        elves += 1
        if elves == 3:
            santaSem.signal()

        mutex.signal()

        print("get help")
        ## using elfTex here to wait for santa to help them
        elfTex.wait()

        mutex.wait()

        elves -= 1
        if elves == 0:
            elfTex.signal()

        mutex.signal()

def setup():
    subscribe_thread(santaThread)
    for i in range(9):
        subscribe_thread(reindeersThread)
    for i in range(3):    
        subscribe_thread(elvesThread)