import random

words = ["python", "javascript", "java", "dotnet"]


rand_word = random.choice(words)
print(rand_word)
word_length = len(rand_word)
# print(word_length)

characters = []
for i in range(0, word_length):
    characters.append("_")
print(" ".join(characters))
guesses = 0
# print('_' not in characters)
while "_" in characters:
    guess = input("enter a guess: ").strip().lower()
    guesses += 1
    if guess == rand_word:
        for i, letter in enumerate(rand_word):
            characters[i] = letter
        print(" ".join(characters))
        break
    if len(guess) != 1:
        print("Enter single letter only")
        continue
    if guess in characters:
        print("Already guessed!")
        continue
    if guess in rand_word:
        # below code only gives first found index so if multiple charactere are there its issue
        # get_index = rand_word.find(guess)
        # characters[get_index] = guess
        for i, letter in enumerate(rand_word):
            if letter == guess:
                characters[i] = guess
    else:
        print("wrong guess Try again!")
    print(" ".join(characters))

print(f"guesses: {guesses}")
print("Hurray You won 🥳!!")
