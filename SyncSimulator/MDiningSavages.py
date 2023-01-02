from Environment import *
from Environment import _blk

def vegetarian_savage_thread():
    while True:
        mutex.wait()
        while not bag.contains("vegetarian"):
            cv_vegetarian.wait()

        bag.get("vegetarian")
        print("Vegetarian eating food")

        if not bag.contains("vegetarian") and bag.size() < 5:
            cv_vegetarian_cook.notify()
        mutex.signal()

        
def vegetarian_cook_thread():
    while True:
        mutex.wait()
        while bag.size() == 5 or bag.contains("vegetarian"):
            cv_vegetarian_cook.wait()

        for i in range(5-bag.size()):
            bag.put("vegetarian")

        print("Vegetarian food is cooked")

        if bag.contains("vegetarian"):
            cv_vegetarian.notify_all()
        mutex.signal()

def carnivore_savage_thread():
    while True:
        mutex.wait()
        while not bag.contains("carnivore"):
            cv_carnivore.wait()

        bag.get("carnivore")
        print("Carnivore eating food")

        if not bag.contains("carnivore") and bag.size() < 5:
            cv_carnivore_cook.notify()
        mutex.signal()

        
def carnivore_cook_thread():
    while True:
        mutex.wait()
        while bag.size() == 5 or bag.contains("carnivore"):
            cv_carnivore_cook.wait()

        for i in range(5-bag.size()):
            bag.put("carnivore")

        print("Carnivore food is cooked")

        if bag.contains("carnivore"):
            cv_carnivore.notify_all()
        mutex.signal()

vegetarian_food = MyInt(0, "Vegetarian Food")
carnivore_food = MyInt(0, "Carnivore Food")
total_food = MyInt(0, "Total Food")
max_size = MyInt(5, "Max Food")
bag = MyBag("Bag")
mutex = MyMutex("Mutex")
cv_vegetarian = MyConditionVariable(mutex, "cv_vegetarian")
cv_carnivore = MyConditionVariable(mutex, "cv_carnivore")
cv_vegetarian_cook = MyConditionVariable(mutex, "cv_vegetaria_cook")
cv_carnivore_cook = MyConditionVariable(mutex, "cv_carnivore_cook")

def setup():
    subscribe_thread(carnivore_cook_thread)
    subscribe_thread(carnivore_savage_thread)
    subscribe_thread(vegetarian_cook_thread)
    subscribe_thread(vegetarian_savage_thread)   