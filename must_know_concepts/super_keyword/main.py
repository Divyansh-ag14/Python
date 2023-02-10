class Parent:
    def func(self):
        print("I am parent class")
        
class Child(Parent):
    def func(self):
        print("method of child class")
        
    def child_method(self):
        print("I am child class!")
        
        super().func()
    
c1 = Child()
c1.child_method()