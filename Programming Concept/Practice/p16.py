# set in python 

collections = {1, 2, 3, 4, 4, "Harish", "Harish"}

print(collections)
print(type(collections)) # class set

print(len(collections))

collection = set() # gives me set not use {} because it is dict
print(type(collection))

# Methods in set : add(el), remove(el), clear(), pop()


collect = set()
collect.add(1)
collect.add(2)
collect.add(3)
collect.add("HarishSemwal")
collect.add((1, 2, 3))
print(collect)

print(len(collect))

collect.pop()

print(len(collect))
print(collect)

# collect.clear()
# print(collect)



