class Person:
    def __init__(self, name, age) -> None:
        self.__name = name 
        self.__age = age
    
    @property 
    def Name(self):
        return self.__name
    
    @property
    def Age(self):
        return self.__age
    
    @Age.setter
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
