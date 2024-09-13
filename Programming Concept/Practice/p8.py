# List In Python

marks = [50, 60, 70, 80, 90, 100];
print(marks)
print(type(marks))
print(len(marks))

# Slicing in list

print(marks[1:4])

#List Methods

marks.append(5)
print(marks)

marks.sort()
print(marks)

marks.sort(reverse= True)
print(marks)

marks.reverse()
print(marks)

marks.insert(4, 2)
print(marks)

marks.remove(2) #Element remove
print(marks)

marks.pop(2) #remove index
print(marks)
