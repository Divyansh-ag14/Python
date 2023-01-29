class Person:
    def __init__(self, name, age):
        # double underscore is used to make data members private
        # now they can not be accessed outside the class directly
        self.__name = name 
        self.__age = age
    
    @property  #getter
    def Name(self):
        return self.__name
    
    @property # getter
    def Age(self):
        return self.__age
    
    @Age.setter # setter
    def Age(self, value):
        if value>0:
            self.__age = value
            
    def show(self): 
        print(self.__name, self.__age)
        
        
p = Person("dan", 22)
p.show()
p.Age = 24
p.show()
p.Age = -1
p.show()
