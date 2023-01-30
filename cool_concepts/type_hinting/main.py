# since python is dynamically type there is no way to check or understand the types of arguemtns passed before run time
# as the name suggests type hinting makes it easy for others to learn about the values of paramaters
# this is done simply by using :
# to highlight the function return type use ->

# function func takes an argument of type int and has a return value of none
def func(param: int) -> None:
    print(param)
    
func(1)
func("divyansh") #does not lead to error

# however we can use type hinting with mypy to fix this
    
    