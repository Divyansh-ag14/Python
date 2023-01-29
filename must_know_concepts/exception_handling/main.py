def func(a,b):
    try:
        print(a/b)
    except Exception as e:
        print("Error occured!", e)
        
    finally:
        print("I am executed no matter what")
        
        
func(2,3)
func(2, "a")        
