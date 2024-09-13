# store marks of 3 subject then find average of those subject

class student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks
    def average(self):
        sum = 0
        for val in self.marks:
            sum += val
        print("The average is: ", sum/3)
    
s1 = student("TonyStark", [98, 94, 95])
s1.average()