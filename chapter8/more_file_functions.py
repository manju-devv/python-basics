# readLines() returns a list of strings, where each string is a line from the file,
# including the newline character at the end of each line.


f = open("file.txt")
content = f.readlines()
print(content)
f.close()


# readLine() reads a single line from the file each time it is called.
# it returns that line as a string, including the newline character at the end of the line.

f = open("file.txt", "r")
line1 = f.readline()
print(line1)

line2 = f.readline()
print(line2)

line3 = f.readline()
print(line3)

line4 = f.readline()
print(line4)

f.close()

# using loop

f = open("file.txt", "r")
line = f.readline()
while line != "":
    print(line)
    line = f.readline()

f.close()



#modes of file handling
# r --> read mode
# w --> write mode
# a --> append mode
# r+ --> read and write mode
# w+ --> write and read mode
# a+ --> append and read mode
# +  --> open for updating (reading and writing)
#rb --> open for read binary mode
#rt --> open for read in text mode
#wb --> open for write in binary mode
#wt --> open for write in text mode
# ab --> open for append in binary mode
# at --> open for append in text mode
# x  --> create mode