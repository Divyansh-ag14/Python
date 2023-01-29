def func():
    if 1:
        raise ValueError("Something went wrong!")
        #raise Exception("Something went wrong!")
    
func()
print("i am never exectued")