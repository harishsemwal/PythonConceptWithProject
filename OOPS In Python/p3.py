# Class & Instance Attribute -: 

class student: 
    def __init__(self, fullname, marks):
        self.name = fullname
        self.marks = marks
    def welcome(self):
        print("welcome to student ", self.name)
        
    def get_marks(self):
        return self.marks
    
s1 = student("karna", 97)
s1.welcome()
print(s1.get_marks())