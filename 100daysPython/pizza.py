print("Welcome to python pizza deliveries!")

bill = 0
size = input("what size pizza do you want? S, M or L: ").lower()
pepperoni = input("Do you want pepperoni on your pizza? Y / N: ").lower()
extra_cheese = input("Do you want extra cheese? Y / N: ").lower()


if size == "s":
    bill += 15
elif size == "m":
    bill += 20
elif size == "l":
    bill += 25
else:
    print("you typed wrong input!")

if pepperoni == "y":
    if size == "s":
        bill += 2
    else:
        bill += 3

if extra_cheese == "y":
    bill += 1


print(f"Your final bill is: {bill}.")
