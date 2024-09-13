# File Input & Output in Python

''' Python Can be Used to Perform I/O Operation on file. '''

# Text File -: .txt, .docx, .log, etc
# Binary Files -: .mp4, .mov, .png.
# Read -: r, Write -: w

f = open("f23.txt", "r")
data = f.read()
fiveLine = f.read(5)
allLine = f.readline()
print(data)
print(type(data))
f.close()

'''
r -> open for reading (default)
w -> open for writing, truncating the file first
x -> create a new file and open it for writing
a -> open for writing, appending to the end of the file if it exists
b -> binary mode
t -> text mode (default)
+ -> open a disk file for updating (reading and writing)

'''