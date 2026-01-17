import random


game_dict = {1: "Snake", 0: "Water", -1: "Gun"}
computer = random.choice([1, 0, -1])
comp_choice = game_dict[computer]

while True:
    user = int(input("Enter 1 for Snake, 0 for Water, -1 for Gun: "))
    if(user in game_dict):
        break;
    print("Invalid input! Please enter 1, 0, or -1.")


user_choice = game_dict[user]
print(f"comp chose {comp_choice} you have chosen {user_choice}")

if comp_choice == user_choice:
    print("It's a tie!")
else:
    if computer == 1 and user == 0:
        print("Computer wins! Snake drinks Water.")
    elif computer == 1 and user == -1:
        print("you win! gun shoots snake.")
    elif computer == 0 and user == 1:
        print("you win! snake drinks water.")
    elif computer == 0 and user == -1:
        print("Computer wins! water damages gun.")
    elif computer == -1 and user == 1:
        print("Computer wins! gun shoots snake.")
    elif computer == -1 and user == 0:
        print("you win! water damages gun.")
    else:
        print("Something went wrong!")
