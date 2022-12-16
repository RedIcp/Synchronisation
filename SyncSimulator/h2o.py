from Environment import *
from Environment import _blk

def oxigenThread():
    while True:
        oPipet.wait()
        
        hTurnstile.signal()
        hTurnstile.signal()
        
        oTurnstile.wait()
        oTurnstile.wait()
        
        oPipet.signal()

def hydroThread():
    while True:
        hPipet.wait()
        
        hTurnstile.signal()
        oTurnstile.signal()
        
        hTurnstile.wait()
        hTurnstile.wait()
        
        hPipet.signal()
        
hPipet = MySemaphore(2, "hPipet")
oPipet = MySemaphore(1, "oPipet")
hTurnstile = MySemaphore(0, "hTurnstile")
oTurnstile = MySemaphore(0, "oTurnstile")

N = 5

def setup():
    for i in range(N):
        subscribe_thread(oxigenThread)
        subscribe_thread(hydroThread)