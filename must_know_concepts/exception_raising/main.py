def func():
    if 1:
        raise Exception("Something went wrong!")
    
func()
print("i am never exectued")