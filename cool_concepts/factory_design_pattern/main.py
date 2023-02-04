from abc import ABCMeta, abstractstaticmethod

# abstarct class
# to highlight a class as interface in python, the convention is to use "I" before its name
class IPerson(metaclass=ABCMeta):
    
    @abstractstaticmethod
    def person():
        """Interface method"""
        
try:
    p = IPerson() # throws error as we cant instantiate an abstract class
except Exception as e:
    print("Cant instantiate IPerson, executing rest of the code :}")
    
class Student(IPerson):
    def __init__(self) -> None:
        self.name = "Divyansh"
    
    # it is must to override the abstract method
    def person(self):
        print("I am a student")
        
class Teacher(IPerson):
    def __init__(self) -> None:
        self.name = "xyz"
        
    def person(self):
        print("I am a teacher")

# decide during run time which child class object to create       
class PersonFactory:
    @staticmethod
    def build_person(person_type: str):
        if person_type == "Student":
            return Student()
        elif person_type == "Teacher":
            return Teacher()
        else:
            return
        

choice = input("Enter type: ")
#PersonFactory.build_person(choice).person()
p = PersonFactory.build_person(choice)
p.person()