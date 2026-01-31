import random


# comp = random.randint(0, 2)
# items = ["apple","banana","kiwi"]
# print(items[comp]);
# print(random.choice(items));

items = ["rock", "paper", "scissor"]
user_choice = input("Enter your choice (rock/paper/scissor): ").lower()
comp_choice = random.choice(items)

print(f"you chose: {user_choice} & computer choice: {comp_choice}")

if user_choice == comp_choice:
    print("It's a tie!!")
elif user_choice == "rock":
    if comp_choice == "paper":
        print("paper wraps rock Computer Wins!!")
    else:
        print("rock smashes scissors You Win!!")
elif user_choice == "paper":
    if comp_choice == "rock":
        print("paper wraps rock You Win!!")
    else:
        print("scissors cuts paper Computer Wins!!")
elif user_choice == 'scissor':
    if(comp_choice == 'rock'):
        print("rock smashes scissors Computer Wins!!")
    else:
        print("scissors cuts paper You Win!!")