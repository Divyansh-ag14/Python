def decorate(func):
    
    def wrapper():
        print("decorating your function!")
        func()
        
    return wrapper

def hello():
    print("hello!")

decorate(hello)()