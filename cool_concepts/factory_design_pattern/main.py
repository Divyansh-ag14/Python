from abc import ABCMeta, abstractstaticmethod

# abstarct class
class IPerson(metaclass=ABCMeta):
    
    @abstractstaticmethod
    def person():
        """Interface method"""
        
p = IPerson() # throws error as we cant instantiate an abstract class