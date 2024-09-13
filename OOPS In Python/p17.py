# property Decorator
# We use @property decorator on any method in the class to use the method as a property.

class student:
    def __init__(self, phy, chem, math):
        self.phy = phy
        self.chem = chem
        self.math = math
        
    @property
    def percentage(self):
        return str((self.phy + self.chem + self.math)/3) + "%"
        
std = student(98, 97, 96)
print(std.percentage)

std.math = 85 
print(std.percentage)

