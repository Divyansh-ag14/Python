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
    
#hello_world()

# the upper decorator function does not work when we have arguments in our functions that we want to decorate
# solution: add *args, **kwargs

def decorater(function):
    
    def wrapper(*args, **kwargs):
        print("decorating your function!")
        function(*args, **kwargs)
        
    return wrapper

@decorater
def hello_user(user):
    print(f"Hello {user}!")

hello_user("divyansh")