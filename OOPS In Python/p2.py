# Constructor in Python

class student:
    # Default Constructor
     def __init__(self):
        print("Default Constructor...")
    # Parameterized
    def __init__(self, fullname, marks):
        self.name = fullname
        self.marks = marks;
        print("Constructor...")
        
        
s1 = student("Karan", 50)
print(s1.name, s1.marks)