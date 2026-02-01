# List comprehension is a short and clean way to create a new list from another list (or iterable) using one line of code.

# Think of it as:

# “a shortcut for writing a loop that builds a list”

my_list = [1, 3, 5, 7, 11]

squared_list = [i * i for i in my_list]
print(squared_list)
