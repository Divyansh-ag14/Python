# use decorator to show execution time of function

import time

def timer(func):
    
    def wrapper(*args, **kwargs):
        print("timing your function!")
        s = time.time()
        val = func(*args, **kwargs)
        e = time.time()
        print(f"function: {func.__name__}")
        print(f"function execution time {e-s} seconds!")
        return val
        
    return wrapper

@timer
def func():
    result=0
    for i in range(1,100000000):
        result+=i
        
    return result

func() 
#print(func())