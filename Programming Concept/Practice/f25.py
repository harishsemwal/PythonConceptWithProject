# Deleting a File -: 

# import os
# os.remove("sample.txt")


# Practice Question

f = open("f25.txt", "w")
f.write("Hi This is Harish Semwal Here....\n This is harish Semwal\n I love You My Bois \n I like Java....\n")


# Where Java is Prasent Convert There Python -: 

# 1-> Read, Changes, Override

with open("f25.txt", "r") as f:
    data = f.read()

new_data = data.replace("Java", "Python")
print(new_data)

with open("f25.txt", "w") as f:
    f.write(new_data)

# Search Word Learning Exist or not

with open("f25.txt", "r") as f:
    data = f.read()

    print(data)
    if(data.find("Learning") != -1):
        print("Prasent...")
    else:
        print("Not Prasent...")

# check Which Line the word Learning Occurs first

word = "harish"
data = True
line_no = 1
with open("f25.txt", "r") as f:
    while data:
        data = f.readline()
        if(word in data):
            print(line_no)
        line_no += 1

# Even Number Count

with open("d100.txt", "r") as f:
    data = f.read()
    print(data)

    num = ""
    for i in range (len(data)):
        if (data[i] == ","):
            print(int(num))
            num = ""
        else:
            num += data[i]
f.close()


with open("d100.txt", "r") as f:
    data = f.read()
    print(data)
    count = 0
    num = data.split(",")
    for val in num:
        if(int(val) % 2 == 0):
            count += 1
        
    print(count)