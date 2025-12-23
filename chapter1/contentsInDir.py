import os;

directory_path = '/Users/manju/Desktop/pythonLearning/chapter1';
contents = os.listdir(directory_path);

for item in contents:
    print(item);