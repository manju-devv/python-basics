# missing number
list = [1, 2, 4, 5]
missing = 0
flag = list[0]

for i in range(len(list)):
    if list[i] == flag:
        flag += 1
    else:
        missing = flag
print(missing)



