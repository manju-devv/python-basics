# try–except in Python is an exception-handling mechanism used to catch and handle runtime errors so
# that the program does not crash and can continue executing normally.


try:
    a = int(input("Enter a number: "))
    print(a)
except Exception as e:
    print(e)
finally:
    print("Thank you")
