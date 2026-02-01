a = 89


def fun():
    global a #sets globally a value like overriding above a 
    a = 3
    print(a)


fun()
print(a)
