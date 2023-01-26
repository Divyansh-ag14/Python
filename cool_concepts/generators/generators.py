# generators are used for on demand sourcing

import sys

def square_generator(n):
    for x in range(1,n):
        yield x*x
        
values = square_generator(8)
for x in values:
    print(x)

# changing the values of params does not change the size of the object
obj1 = square_generator(8)
obj2 = square_generator(16)
print(sys.getsizeof(obj1))
print(sys.getsizeof(obj2))


# working of yield and next
def gen():
    num=1
    print("first execution")
    yield num
    
    num=10
    print("second execution")
    yield num
    
    num=100
    print("third execution")
    yield num
    
# obj = gen()
# print(next(obj))
# print(next(obj))
# print(next(obj))
    