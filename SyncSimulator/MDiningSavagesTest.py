from Environment import *
from Environment import _blk

def savageThread(diet_type):
    while True:
        mu.wait()
        # while not enough food for all savages or 
        # food not correspondant to savage diet, 
        # savage wait
        mu.signal()
        # eating corresponding diet, remove 1 from bag 
        # (more than 1 savage can be eating)
        mu.wait()
        # if pot empty after eating, notify cook, 
        # else notify cook of corresponding diet
        mu.signal()
        
def cookThread(diet_type):
    while True:
        # only one cook can be using the pot?
        mu.wait()
        # while pot not empty, wait
        
        # preparing food for corresponding diet, addd 1 to bag
        
        # notify all savages
        mu.signal()

class Savage:
    def __init__(self, diet_type):
        self.diet_type = diet_type

class Cook:
    def __init__(self, diet_type):
        self.diet_type = diet_type
        
bag = MyBag("MyBag")
#bagEmpty = MyBool(False, "bagEmpty")
mu = MyMutex("mutex")
pot = MyConditionVariable(mu, "pot")

numVegetarianSavages = 2
vegetarian = MyConditionVariable(mu, "vegetarian")
vegetarianSavages = [Savage(vegetarian) for i in range(numVegetarianSavages)]

numCarnivoreSavages = 2
carnivore = MyConditionVariable(mu, "carnivore")
carnivoreSavages = [Savage(carnivore) for i in range(numCarnivoreSavages)]

vegetarianCook = Cook(vegetarian)
carnivoreCook = Cook(carnivore)
    
def setup():
    subscribe_thread(lambda: cookThread(vegetarianCook))
    subscribe_thread(lambda: cookThread(carnivoreCook))
    
    for i in range(numVegetarianSavages):
        subscribe_thread(lambda: savageThread(vegetarianSavages))
        
    for i in range(numCarnivoreSavages):
        subscribe_thread(lambda: savageThread(carnivoreSavages))