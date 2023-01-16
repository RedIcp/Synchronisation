def threadWriter():
    while True:
        mutex.wait()
        writers_wait.v += 1
        while not (readers_busy.v == 0 and writers_busy.v == 0):
            cv_writer.wait()
        writers_wait.v -= 1
        writers_busy.v+=1
        mutex.signal()
        print("writer is writing")
        mutex.wait()
        writers_busy.v-=1
        if writers_busy.v == 0:
            print("Writer left")
            if writers_wait.v > 0 and writer_prio.v:
                cv_writer.notify()
            elif readers_wait.v > 0:
                cv_reader.notify_all()
            elif writers_wait.v > 0:
                cv_writer.notify()
        mutex.signal()
def threadReader():
    while True:
        mutex.wait()
        readers_wait.v += 1
        while not writers_busy.v == 0:
            cv_reader.wait()
        readers_wait.v -= 1
        readers_busy.v += 1
        mutex.signal()
        print("readers are reading")
        mutex.wait()
        readers_busy.v-=1
        if readers_busy.v == 0:
            print("All readers left")
            if writers_wait.v > 0:
                cv_writer.notify()
        mutex.signal()

from Environment import *




readers_busy = MyInt(0, "Readers Busy")
writers_busy = MyInt(0, "Writers Busy")
readers_wait = MyInt(0, "Readers Waiting")
writers_wait = MyInt(0, "Writers Waiting")
writer_prio = MyBool(True, "Is writer priotised")
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