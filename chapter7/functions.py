# function definition


def func1():
    print("Hello world")


func1()  # function call


def avg():
    a = int(input("enter first num: "))
    b = int(input("enter second num:"))
    c = int(input("enter third num:"))
    average = (a + b + c) / 3
    print(f"average of {a}, {b}, {c} is {average}")


avg()


# there are two types of functions
# inbuilt functions [like print(), input(), int(), already available in python]
# user defined functions [written by user]

# function with arguments


def goodDay(name, greet):
    print(f"Good day {name},{greet} all day")


goodDay("manju", "shine")


def default(name, greet="Have a wonderful day!"):
    print(f"Good day {name},{greet} sun shines!")


default("manju");
default("Harry", "keep smiling!")
