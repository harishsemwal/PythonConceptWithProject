# static Methods 
# static methods are methods that do not use self parameter

class student:
    @staticmethod
    def hello():
        print("Hello")

s = student()
s.hello()