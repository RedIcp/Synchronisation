from Environment import *
from Environment import _blk

def vegetarian_savage_thread():
    while True:
        mutex.wait()
        while vegetarian_food.v == 0:
            cv_vegetarian.wait()

        vegetarian_food.v -= 1
        total_food.v -= 1
        print("Vegetarian eating food")

        if vegetarian_food.v == 0 and total_food.v < max_size.v:
            cv_vegetarian_cook.notify()
        mutex.signal()

        
def vegetarian_cook_thread():
    while True:
        mutex.wait()
        while total_food.v == max_size.v or vegetarian_food.v > 0:
            cv_vegetarian_cook.wait()

        vegetarian_food.v = max_size.v - total_food.v
        total_food.v = max_size.v
        print("Vegetarian food is cooked")

        if vegetarian_food.v > 0:
            cv_vegetarian.notify_all()
        mutex.signal()

def carnivore_savage_thread():
    while True:
        mutex.wait()
        while carnivore_food.v == 0:
            cv_carnivore.wait()

        carnivore_food.v -= 1
        total_food.v -= 1
        print("Carnivore eating food")

        if carnivore_food.v == 0 and total_food.v < max_size.v:
            cv_carnivore_cook.notify()
        mutex.signal()

        
def carnivore_cook_thread():
    while True:
        mutex.wait()
        while total_food.v == max_size.v or carnivore_food.v > 0:
            cv_carnivore_cook.wait()

        carnivore_food.v = max_size.v - total_food.v
        total_food.v = max_size.v
        print("Carnivore food is cooked")

        if carnivore_food.v > 0:
            cv_carnivore.notify_all()
        mutex.signal()

vegetarian_food = MyInt(0, "Vegetarian Food")
carnivore_food = MyInt(0, "Carnivore Food")
total_food = MyInt(0, "Total Food")
max_size = MyInt(5, "Max Food")
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