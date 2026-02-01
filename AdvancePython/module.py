# def myFunc():
#     print("Hello World!!")
#     print(__name__)  # will print module if it is executed from another file
#     # will print __main__ if code is executed in parent file


# myFunc()


def myFunc():
    print("Hello World!!")


if __name__ == "__main__":
    print("we're directly running this code")
    myFunc()
    print(__name__)
