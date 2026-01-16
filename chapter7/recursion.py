# recursion is a function that calls itself


def factorial(n):
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)


a = int(input("enter a num: "))
print(f"The factorial of {a}: {factorial(a)}")


# recursion to find sum of n numbers


def sum(n):
    if n == 1:
        return 1
    return n + sum(n - 1)


b = int(input("enter a num: "))
print(f"The sum of {b} numbers is: {sum(b)}")


def print_stars(n):
    if n == 0:
        return
    print("*"*n)
    print_stars(n - 1)


stars = int(input("enter number of stars: "))
print_stars(stars)
