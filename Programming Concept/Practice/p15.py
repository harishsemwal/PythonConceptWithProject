# Dictonary Methods

dict = {
    "name" : "Harish", 
    "learning":"Python",
    "age" : 22, 
    "subject" : ["Python", "C++"],
    "topics": ("dict", "set"),
}

print(dict.keys())
print(list(dict.keys()))

print(dict.values())
print(list(dict.values()))

print()
print()

pairs = list((dict.items()))
print(pairs[0])

print()
print()

# get
print(dict["name"])
print(dict.get("name2")) #ager name2 nahi prasent hoga to none dega na ki error


dict.update({"age":23})
print(dict)
