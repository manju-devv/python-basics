data = input("Enter some data to write into file: ")
f = open("fileWrite.txt", "w")
f.write(data)
f.close()
