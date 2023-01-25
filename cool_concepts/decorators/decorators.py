def decorate(func):
    
    def wrapper():
        print("decorating your function!")
        func()
        
    return wrapper

def hello():
    print("hello!")

# not the right way
#decorate(hello)()

@decorate
def hello_world():
    print("Hello World!")
    
hello_world()

