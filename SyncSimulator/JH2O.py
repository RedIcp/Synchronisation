from Environment import *
from Environment import _blk

def oxygenThread():
    while True:
        oPipet.wait()
        
        oTurnstile.wait()
        oTurnstile.wait()

        hTurnstile.signal()
        hTurnstile.signal()
        
        oPipet.signal()
        print("Got 1 Oxygen")

def hydrogenThread():
    while True:
        hPipet.wait()
        
        hTurnstile.signal()
        oTurnstile.signal()
        
        hTurnstile.wait()
        hTurnstile.wait()
        
        hPipet.signal()
        print("Got 1 Hydrogen")
        
hPipet = MySemaphore(2, "hPipet")
oPipet = MySemaphore(1, "oPipet")
hTurnstile = MySemaphore(0, "hTurnstile")
oTurnstile = MySemaphore(0, "oTurnstile")

N = 5

def setup():
    for i in range(N):
        subscribe_thread(oxygenThread)
        subscribe_thread(hydrogenThread)