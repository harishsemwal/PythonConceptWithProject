# del Keyword
# used to delete object properties or object itself

class student:
    def __init__(self, name):
        self.name = name
        
s1 = student("Harish")
print(s1.name)
del s1.name
print(s1.name) # new it dose not access