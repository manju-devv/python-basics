# print("Welcome to Treasure Island.Your mission is to find the treasure.")

# direction = input("please enter 'left' or 'right': ").lower()


# if direction != "right":
#     print("Fall into a hole. Game Over.")
# else:
#     print("you have reached river")
#     reach_to_island = input("Do you want to 'swim' or 'wait': ").lower()
#     if reach_to_island != "wait":
#         print("Attacked by trout. Game Over")
#     else:
#         print("you have reached island unharmed!")
#         choice = input("select 'red' / 'blue' / 'yellow' door: ").lower()
#         if choice == "red":
#             print("Burned by fire. Game Over.")
#         elif choice == "blue":
#             print("Eaten by beasts. Game Over")
#         elif choice == "yellow":
#             print("you have found the treasure")
#         else:
#             print("Game over!")


print(
    '''
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/________

'''
)

print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.\n")

direction = input("Choose a direction (left / right): ").strip().lower()

if direction != "right":
    print("You fell into a hole. Game Over.")
    exit()

print("You reached a river.")

reach_to_island = input("Do you want to swim or wait? ").strip().lower()

if reach_to_island != "wait":
    print("Attacked by trout. Game Over.")
    exit()

print("You arrived at the island unharmed!")

choice = input("Choose a door (red / blue / yellow): ").strip().lower()

if choice == "red":
    print("Burned by fire. Game Over.")
elif choice == "blue":
    print("Eaten by beasts. Game Over.")
elif choice == "yellow":
    print("🎉 You found the treasure! You win!")
else:
    print("Invalid choice. Game Over.")


# https://ascii.co.uk/art/treasure
