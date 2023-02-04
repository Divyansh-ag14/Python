# create objects of child class dynamically

from abc import ABCMeta, abstractstaticmethod

class IPerson(metaclass = ABCMeta):
    
    @abstractstaticmethod
    def person():
        pass
    
class Student(IPerson):
    def __init__(self):
        self.name = "Divyansh"
        
    def person(self):
        print("I am a student")
        
class Teacher(IPerson):
    def __init__(self):
        self.name = "xyz"
        
    def person(self):
        print("I am a teacher")

class PersonFactory:
    @staticmethod
    def build_person(type: str):
        # globals() returns dictionary of global variables
        return globals()[type]() # returns object of defined child class
    
objs = ["Student", "Teacher"]
for obj in objs:
    PersonFactory.build_person(obj).person()