import random
from hangman_words import words,stages;




chosen_word = random.choice(words)
print(chosen_word)

place_holder = "_ " * len(chosen_word)
print(place_holder)

game_over = False
correct_letters = []
lives = 6
while not game_over:
    guess = input("Guess the letter in the word: ").lower()
    if guess in correct_letters:
        print(f"you have already guessed the letter {guess}")
    if guess not in chosen_word:
        lives -= 1
        if lives == 0:
            game_over = True;
            print(stages[6 - lives])
            print(f"you died !Game Over, the word is {chosen_word}")
            break

    display = ""
    for letter in chosen_word:
        if letter == guess:
            display += letter
            correct_letters.append(letter)
        elif letter in correct_letters:
            display += letter
        else:
            display += " _ "
    print(display)
    print(stages[6 - lives])
    print(f"you still have {lives} lives")
    if " _ " not in display:
        game_over = True
        print("You won the game!")
