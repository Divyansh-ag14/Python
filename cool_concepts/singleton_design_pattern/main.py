# the idea is to instantiate the class only once

from abc import ABCMeta, abstractstaticmethod

class IPerson(metaclass=ABCMeta):
    @abstractstaticmethod
    def print_data():
        pass
    
class PersonSingleton(IPerson):
    
    __instance=None
    
    def __init__(self, name, age):
        if PersonSingleton.__instance != None:
            raise Exception("Singleton can not be instantiated more then 1") 
        
        else:
            self.name=name
            self.age=age
            PersonSingleton.__instance = self
    
    
    @staticmethod
    def get_instance():
        if PersonSingleton.__instance == None:
            return PersonSingleton("defualt name", 0)
        return PersonSingleton.__instance
    
    def print_data(self):
        print(f"Name: {self.name} Age: {self.age}")
        
p = PersonSingleton("divyansh", 22)
print(p)
p.print_data()
# p2 = PersonSingleton("abc", 11) raises exception
p2 = PersonSingleton.get_instance()
print(p2) # same as p