# class method -> 

# A class method is bound to the class & receives the class as an implicit first argument.

# Note - static method can't access or modify class state & generally for utility.

class Person:
    name = "anonymous"
    
    # def changeName(self, name):
        # self.__class__.name = "Rahul" || # Ye Class name ko bhi modify kar deta hai....
        
    @classmethod
    def changeName(cls, name):
        cls.name = name
        
    
p1 = Person()
p1.changeName("Rahul Kumar")

print(p1.name)
print(Person.name)
