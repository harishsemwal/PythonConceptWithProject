# Super In OOPS in python
class Car:
    def __init__ (self, type):
        self.type = type
        
    @staticmethod
    def start():
        print("Car Started...")
        
class ToyotaCar(Car):
    def __init__(self, name, type):
        self.name = name
        super().__init__(type)
        
c1 = ToyotaCar("Prius", "Electric")
print(c1.type)