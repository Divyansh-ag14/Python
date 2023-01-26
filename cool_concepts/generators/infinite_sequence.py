def infinite_seq():
    x=1
    while True:
        yield x*x
        x+=1
        
vals = infinite_seq()
for x in range(10):
    print(next(vals))
        
    