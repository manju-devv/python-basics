# The Random Access Memory is Volatile and all its contents are lost once a program.
# Inorder to persist data forever we use files.

# A file is data stored in storage device. A py program can talk to the file by reading  and writing content to it


# types of files 
# text files --> .txt, .py, .c etc
# binary files --> .jpg, .png, .exe etc



f = open("file.txt","r"); #read mode
data = f.read();
print(data);
f.close();