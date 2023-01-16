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
            student.signal(total_students)
        mutex.signal()
        
        teacherTeaches.wait()

        classroom_open.v = False

def studentThread():
    while True:
        mutex.wait()
        nr_of_students_present.v += 1
        if nr_of_students_present.v == 3 and not classroom_open.v:
            teacher.signal()
        mutex.signal()

        print("Waiting for classroom to be open")
        student.wait()

        if classroom_open.v:
            print("Listen to lecture")

        mutex.wait()
        nr_of_students_present.v -= 1
        
        if nr_of_students_present.v == 0:
            teacherTeaches.signal()
        mutex.signal()



nr_of_students_present = MyInt(0, "Number of students")
total_students = 10
classroom_open = MyBool(False, "Open/Close")
teacher = MySemaphore(0, "Teacher")
teacherTeaches = MySemaphore(0, "Teacher teaches")
student = MySemaphore(0, "Student")
mutex = MySemaphore(1, "Mutex")

def setup():
    subscribe_thread(teacherThread)
    for i in range(total_students):    
        subscribe_thread(studentThread)