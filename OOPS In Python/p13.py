# Multilevel Inheritance
class car:
    @staticmethod
    def start():
        print("car started..")
    
    @staticmethod
    def stop():
        print("car stopped..")
        
class ToyotaCar(car): #inheritance
    def __init__(self, brand):
        self.brand = brand
        
class Fortunure(ToyotaCar):
    def __init__(self, type):
        self.type = type

car1 = Fortunure("Diesal")
car1.start()