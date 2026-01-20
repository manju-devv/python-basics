# with will automatically handle closing the file for you, even if exceptions occur.


with open("file.txt", "r") as f:
    content = f.read()
    print(content)
