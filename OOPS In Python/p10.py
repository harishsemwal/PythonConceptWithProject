# Private Keyword in Python OOP -: 

# Conceptual Implementations in Python
# Private attributes & methods are meant to be used only within the class and are not accessible from outside the class.

# __ <- this matlb private

class account:
    def __init__(self, acc_no, acc_pass):
        self.acc_no = acc_no
        self.__acc_pass = acc_pass
    def reset_pass(self):
        print(self.__acc_pass)

acc = account("12345", "abcde")        
print(acc.acc_no)
print(acc.reset_pass())