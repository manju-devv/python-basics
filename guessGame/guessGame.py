from random import randint


n = randint(1, 50)
a = -1
no_of_guesses = 0
print("Welcome to guessing game")
while a != n:
    a = int(input("Enter a number: "))
    if a > n:
        print("Lower number please")
    elif a < n:
        print("Higher number please")
    no_of_guesses += 1

print(f"you have guessed the number {n} correctly in {no_of_guesses} guesses")
# again = input("Do you want to play again (Y/N): ")
# if again.lower() == "y":
#     a = -1
# else:
#     pass
