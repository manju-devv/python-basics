name = input("Enter name of student: ")
marks = int(input("Enter marks: "))
phone = int(input("Enter phone num: "))


s = "The name of student is {}, he got {} marks and his contact details are {}.".format(
    name, marks, phone
)

print(s)
