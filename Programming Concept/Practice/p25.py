# Files With Syntax

with open("f25.txt", 'r') as f:
    data = f.read()
    print(data)


with open("f25.txt", 'w') as f:
    f.write("new Data...")