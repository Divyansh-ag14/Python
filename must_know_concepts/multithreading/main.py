import threading

def func1():
    for i in range(5):
        print("func1")
        
def func2():
    for i in range(5):
        print("func2")
    
t1 = threading.Thread(target=func1)
t2 = threading.Thread(target=func2)

# .start() is used to run threads parallely
# t1.start()
# t2.start()

#t1.start() 
#print("some code") # this statement does not wait for the above thread to finish

# .join() is used to wait for threads
# it makes the main thread wait until specified thread is executed
t1.start()
t1.join()
print("executed after t1")