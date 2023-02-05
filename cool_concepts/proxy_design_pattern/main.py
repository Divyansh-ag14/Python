# the idea is to introduce a middle man

from abc import ABCMeta, abstractstaticmethod

class IPerson(metaclass = ABCMeta):
    @abstractstaticmethod
    def person_func():
        pass
    
class Person(IPerson):
    def person_func(self):
        print("I am a person")

#p1 = Student() # we do not want direct instantiation

class ProxyPerson(IPerson):
    def __init__(self) -> None:
        self.person = Person()
        
    def person_func(self):
        print("Running Proxy")
        self.person.person_func()

p1 = ProxyPerson()
p1.person_func()