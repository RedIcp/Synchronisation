from Environment import *
from Environment import _blk
def teacherThread():
    while True:
        print("Teacher arrives")
        teacher.wait()

        mutex.wait()
        if nr_of_students_present.v >= 3 and not classroom_open.v:
            classroom_open.v = True
            print("Open classroom")
            student.signal(nr_of_students_present.v)
        mutex.signal()
        
        while nr_of_students_present.v > 0: 
            print("Gives lectures")

        classroom_open.v = False

def studentThread():
    while True:
        mutex.wait()
        nr_of_students_present.v += 1
        if nr_of_students_present.v == 3 and not classroom_open.v:
            teacher.signal()
        mutex.signal()

        if not classroom_open.v:
            print("Waiting for classroom to be open")
            student.wait()

        if classroom_open.v:
            print("Listen to lecture")

        mutex.wait()
        nr_of_students_present.v -= 1
        mutex.signal()



nr_of_students_present = MyInt(0, "Number of students")
classroom_open = MyBool(False, "Open/Close")
teacher = MySemaphore(0, "Teacher")
student = MySemaphore(0, "Student")
mutex = MySemaphore(1, "Mutex")

def setup():
    subscribe_thread(teacherThread)
    for i in range(3):    
        subscribe_thread(studentThread)