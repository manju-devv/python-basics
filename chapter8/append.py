string = "this line will be appended to the file\n"

f = open("file.txt", "a")
f.write(string)
f.close()
