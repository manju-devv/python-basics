# try:
#     a = int(input("enter a number: "))
#     print(a)
# except Exception as e:
#     print(e)
# finally:
#     print("i'm being executed finally")

# without finally also above code runs and displays the content taht is used in finally block
# but finally is used in functions and when function returns something  in try or except then next lines of code never runs right
# so finally is used so even function returns finally is executed


def main():
    try:
        a = int(input("enter a number: "))
        print(a)
        return
    except Exception as e:
        print(e)
        return

    finally:
        print("i'm being executed finally")  # it runs

    print("i'm being executed finally")  # never runs


main()
