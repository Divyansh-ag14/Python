
# double underscore methods
class Student:
    def __init__(self, age, name): # constructor
        self.age = age
        self.name = name
        
    def __del__(self):
        print("Object deleted")
        
s1= Student(22, "divyansh")
print(s1.age)
print(s1.name)