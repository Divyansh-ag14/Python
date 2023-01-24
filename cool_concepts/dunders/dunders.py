# double underscore methods


class Student:
    def __init__(self, age, name): # constructor
        self.age = age
        self.name = name
        
    def __del__(self): # deconstructor
        print("Object deleted") 
        
s1= Student(22, "divyansh")
print(s1.age)
print(s1.name)


# operator overloading
class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, vectortypeobj):
        return Vector(self.x+vectortypeobj.x, self.y+vectortypeobj.y)
    
    def __repr__(self): # reperesents how object is printed
        return f"x = {self.x} | y = {self.y}"
        
v1 = Vector(1,2)
v2 = Vector(3,4)
v3 = v1+v2 # gives error if + is not overloaded with the help of __add__()
print(f"v3 = {v3.x, v3.y}")
print(v3)