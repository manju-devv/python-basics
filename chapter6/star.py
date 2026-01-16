no_of_stars = int(input("enter columns: "))
for i in range(1, no_of_stars + 1):
    print(" " * (no_of_stars - i), end="")
    print("*" * (2 * i - 1))


n = int(input("enter a num: "))
for i in range(1, n + 1):
    if i == 1 or i == n:
        print("*" * n, end="")
    else:
        print("*", end="")
        print(" " * (n - 2), end="")
        print("*", end="")
    print("")


table = int(input("enter a number: "))
for i in range(1, 11):
    print(f"{table} X {11 - i} = {table * (11 - i)}")
