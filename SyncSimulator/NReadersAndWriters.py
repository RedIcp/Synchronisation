from Environment import *
from Environment import _blk

def threadReader():
    while True:
        mutex.wait()
        while not writers_busy.v == 0:
            readers_busy.v += 1
            cv_reader.wait()

        readers_busy.v+=1
        mutex.signal()
        
        print("readers are reading")

        mutex.wait()
        readers_busy.v-=1

        if readers_busy.v == 0:
            cv_writer.notify()
        mutex.signal()


def threadWriter():
    while True:
        mutex.wait()
        while not (readers_busy.v == 0 and writers_busy.v == 0):
            writers_busy.v += 1
            cv_writer.wait()

        writers_busy.v+=1
        print("writer is writing")
        writers_busy.v-=1

        if writers_busy.v == 0:
            if writer_prio.v:
                cv_writer.notify()
            else:
                cv_reader.notify_all()
        mutex.signal()



readers_busy = MyInt(0, "Readers Busy")
writers_busy = MyInt(0, "Writers Busy")
readers_wait = MyInt(0, "Readers Waiting")
writers_wait = MyInt(0, "Writers Waiting")
writer_prio = MyBool(False, "Is writer priotised")
mutex = MyMutex("Mutex")
cv_reader = MyConditionVariable(mutex, "cvReader")
cv_writer = MyConditionVariable(mutex, "cvWriter")


def setup():
    subscribe_thread(threadWriter)
    subscribe_thread(threadWriter)
    subscribe_thread(threadWriter)
    subscribe_thread(threadReader)    
    subscribe_thread(threadReader)
    subscribe_thread(threadReader)