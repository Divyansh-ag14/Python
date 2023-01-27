import sys

# when we run "python main.py xyyz" on console
print(sys.argv[0]) # prints "main.py"
print(sys.argv[1]) #prints "xyz"

#print the entire argument vector
print(sys.argv)

# writing to a new file using console
file = sys.argv[1]
msg = sys.argv[2:]

with open(file, 'w+') as f:
    f.write(" ".join(msg))