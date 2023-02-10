class Parent:
    def func(self):
        print("I am parent class")
    
    def hello(self):
        print("hello")
        
class Child(Parent):
    def func(self):
        print("method of child class")
        
    def child_method(self):
        self.func()
        #print("I am child class!")
        super().func()
    
c1 = Child()
c1.child_method()
# c1.hello()
print("")
# calling constructor of parent
class A:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        
class B(A):
    def __init__(self, name, age, gender):
        super().__init__(name, age)
        self.gender = gender
        
    def print_details(self):
        print(self.name)
        print(self.age)
        print(self.gender)
        
obj = B("divyansh", 22, "M")
obj.print_details()