# Polymorphism -: 
# Dender Function -> __add__(b)
# Operator Overloading -: 

class Complex:
    def __init__(self, real, img):
        self.real = real
        self.img = img
        
    def showNumber(self):
        print(self.real, "i +", self.img, "j")
        
    # def add(self, num2):
    #     numReal = self.real + num2.real
    #     numImg = self.img + num2.img
    #     return Complex(numReal, numImg)
    
    def __add__(self, num2):
        numReal = self.real + num2.real
        numImg = self.img + num2.img
        return Complex(numReal, numImg)
    
    def __sub__(self, num2):
        numReal = self.real - num2.real
        numImg = self.img - num2.img
        return Complex(numReal, numImg)
        
num1 = Complex(1, 3)
num1.showNumber()

num2 = Complex(7, 5)
num2.showNumber()

# num3 = num1.add(num2)
# num3.showNumber()

num3 = num1 + num2
num3.showNumber()

print("Substraction: ")
num4 = num1 - num2
num4.showNumber()