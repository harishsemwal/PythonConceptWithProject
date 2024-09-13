# Let's Practice
# Qs. Define a Circle class to create a circle with radius r using the constructor.
# Define an Area() method of the class which calculates the area of the circle.
# Define a Perimeter() method of the class which allows you to calculate the perimeter of the
# circle.

#-------------------------------#-------------------#--------------------------#

# Let's Practice
# Qs. Create a class called Order which stores item & its price.
# Use Dunder function _ _ gt _ ) to convey that:
# orderl > order2 if price of orderl > price of order2

class Order:
    def __init__(self, item, price):
        self.item = item
        self.price = price

    def __gt__(self, odr2):
        return self.price > odr2.price

odrl = Order("chips", 20)
odr2 = Order("tea", 15)
print(odrl > odr2)  # True