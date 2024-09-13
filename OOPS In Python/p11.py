# Inheritance

# -> Multiple Inheritance -> 
class car:
    @staticmethod
    def start():
        print("car started..")
    
    @staticmethod
    def stop():
        print("car stopped..")
        
class ToyotaCar(car): #inheritance
    def __init__(self, name):
        self.name = name
        
        
class company():
    
print(car1.name)
car1.start()