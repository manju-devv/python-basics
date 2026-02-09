import random

rock = """
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
"""

paper = """
    
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
"""

scissors = """
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""

items = [rock, paper, scissors]

user_choice = int(input("enter 0 for rock, 1 for paper, 2 for scissors: \n"))
comp_choice = random.randint(0, 2)

print("computer choice :" + items[comp_choice])
print("your choice :" + items[user_choice])

if user_choice < 0 or user_choice > 2:
    print("Invalid number! You Lose!!")
if user_choice == 0 and comp_choice == 2:
    print("you won!")
elif user_choice == 2 and comp_choice == 0:
    print("computer wins!!")
elif comp_choice > user_choice:
    print("computer wins!!")
elif user_choice > comp_choice:
    print("you won!")
else:
    print("It's a draw!!")





# import random

# rock = """
#     _______
# ---'   ____)
#       (_____)
#       (_____)
#       (____)
# ---.__(___)
# """

# paper = """
#      _______
# ---'    ____)____
#            ______)
#           _______)
#          _______)
# ---.__________)
# """

# scissors = """
#     _______
# ---'   ____)____
#           ______)
#        __________)
#       (____)
# ---.__(___)
# """

# items = [rock, paper, scissors]
# names = ["Rock", "Paper", "Scissors"]

# # User input
# user_choice = int(input("Enter 0 for Rock, 1 for Paper, 2 for Scissors:\n"))

# # Validate input
# if user_choice not in [0, 1, 2]:
#     print("Invalid input! Please choose 0, 1, or 2.")
#     exit()

# # Computer choice
# comp_choice = random.randint(0, 2)

# print(f"\nYou chose {names[user_choice]}:")
# print(items[user_choice])

# print(f"Computer chose {names[comp_choice]}:")
# print(items[comp_choice])

# # Result logic using modulo (magic line ✨)
# result = (user_choice - comp_choice) % 3

# if result == 0:
#     print("It's a draw!")
# elif result == 1:
#     print("You win! 🎉")
# else:
#     print("Computer wins! 🤖")
