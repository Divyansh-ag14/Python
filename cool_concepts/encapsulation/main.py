class Person:
    def __init__(self, name, age):
        # double underscore is used to make data members private
        # now they can not be accessed outside the class directly
        self.__name = name 
        self.__age = age
    
    # static methods do not need to be called from objects 
    # they cam be directly accessed using the class name
    # they can work without passing the self argument
    @staticmethod
    def hello():
        print("Hello world")
    
    @property  #getter
    def Name(self):
        return self.__name
    
    @property # getter
    def Age(self):
        return self.__age
    
    @Age.setter # setter
    def Age(self, value):
        if value>0:
            print("making updates")
            self.__age = value
        else:
            print("Age remains same")
        
            
    def show(self): 
        print(self.__name, self.__age)
        

Person.hello()     
p = Person("dan", 22)
#print(p.Name)
#print(p.Age)
p.show()
p.Age = 24
p.show()
p.Age = -1
p.show()

