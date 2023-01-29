def func(a,b):
    try:
        a=int(a)
        b=int(b)
        print(f"{a}/{b} = {a/b}")
    except Exception as e:
        print("Error occured!", e)
        print("press q to quit")
        val = input(f"Enter a new value for {b}: ")
        if val == "q":
            return
        # val=int(val)
        func(a,val)
        
    finally:
        print("I am executed no matter what")
        

func(2, "a")        
