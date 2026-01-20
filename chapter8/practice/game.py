import random


def game():
    print("Entering the game...")
    score = random.randint(1, 70)
    print(f"Your score is: {score}")
    with open("score.txt", "r") as f:
        high_score = f.read()
        if high_score == "":
            high_score = 0
        else:
            high_score = int(high_score)
    if score > high_score:
        with open("score.txt", "w") as f:
            f.write(str(score))
        print("Congratulations! You have the new high score!")


game()
