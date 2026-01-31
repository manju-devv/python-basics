# 🦭 Walrus Operator (:=)

# The walrus operator (:=) is called the assignment expression operator.
# It lets you assign a value to a variable and use that value in the same expression.

# allows you to assign value to variable as a part of expression


# without walrus
# data = input("Enter text: ")
# if data != "":
#     print(data)


# with walrus

# if (data := input("Enter text: ")) != "":
#     print(data)


if(n := len([1,2,3,4,5]) > 3):
    print(f"the length of aray is {5} expected length is {3}")