# since python is dynamically type there is no way to check or understand the types of arguemtns passed before run time
# as the name suggests type hinting makes it easy for others to learn about the values of paramaters
# this is done simply by using :

def func(param: int):
    print(param)
    
func(1)
func("divyansh")
    
    