# generators are used for on demand sourcing

def square_generator(n):
    for x in range(1,n):
        yield x*x
        
values = square_generator(8)
for x in values:
    print(x)

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
    