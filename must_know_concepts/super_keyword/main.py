class Parent:
    def parent_method(self):
        print("I am parent class")
        
class Child(Parent):
    def child_method(self):
        print("I am child class!")
        
        super().parent_method()
    
c1 = Child()
c1.child_method()