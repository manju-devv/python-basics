# with open("log.txt","r") as f:
#     content = f.read();

# if('python' in content):
#     print("the word 'python' is present in the log file")
# else:
#     print("the word 'python' is not present in the log file")


with open("log.txt", "r") as f:
    content = f.readlines()

lineNum = 1

for line in content:
    if "python" in line:
        print(f"the word 'python' is present in line {lineNum}")
        break
    lineNum += 1
else:
    print("search completed & 'python' not found in the file.")
