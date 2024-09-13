# Functions In Python

# Block of statement that perform spacific task

def sum(a, b):
    return a + b

print(sum(5, 6))

# Recusion

print("Recusion")
def show(n):
    if(n == 0):
        return
    print(n)
    show(n-1)

print(show(5))