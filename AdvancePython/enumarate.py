# enumerate() is a built-in Python function that adds an automatic counter (index)
# to an iterable and returns it as an enumerate object, producing (index, value) pairs during iteration.

fruits = ["apple", "banana", "kiwi", "jack fruit"]

for index,item in enumerate(fruits):
    print(f"{index} - {item}")



for i, fruit in enumerate(fruits, start=1):
    print(i, fruit)