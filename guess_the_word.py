# CIS256 33975 FALL 2025    
# EX 4
# ---

# fist task the program will select a random word from a predefined list 
import random

# Becuase are predined words i will create a list of Football teams
The_words_list = ["Barcelona", "Ajax", "Arsenal", "Milan", "Juventus", "Paris", "Liverpool", "Chelsea", "Bayern", "Inter"]
# The user will guesses one letter at a time

def user_get_random_word():
    return random.choice(The_words_list)

# Know i will add def play wher i will add the main logic of the game
# The user will have only 6 attempts to guess the word
def user_play():
    word_to_guess = user_get_random_word()
    revealed_word = ["_"] * len(word_to_guess)
    user_attempts = 6
    user_guessed_letters = set()

    print("--- Welcome to the guess game! ---")
    print ("You only have 6 attempts to guess the word.")

# I will add the while loop to continue the game
    while user_attempts > 0 and "_" in revealed_word:
        print("Current word: " + " ".join(revealed_word))
        print(f"Attempts remaining: {user_attempts}")
        user_guess = input("Guess a letter: ").strip()
# If the user inputs more than one letter or a non-alphabetic character, prompt them to enter a valid guess
        if len(user_guess) != 1 or not user_guess.isalpha():
            print("Please enter a single letter.")
            continue
# IF statement to check if the user has already guessed the letter
        if user_guess in user_guessed_letters:
            print("You already guessed that letter. Try again.")
            continue

        user_guessed_letters.add(user_guess)

        if user_guess in word_to_guess:
            for index, letter in enumerate(word_to_guess):
                if letter == user_guess:
                    revealed_word[index] = user_guess
            print("Good guess!")
        else:
            user_attempts -= 1
            print("Wrong guess.")

# now i if not the user has guessed the word
    if "_" not in revealed_word:
        print("⚽ Well done! 🥅 You guessed the word: " + word_to_guess)
    else:
        print("RED CARD. The correct Football Team was: " + word_to_guess)
# And finally i will add the main function to start the game
if __name__ == "__main__":
    user_play()
# Now let's work on the test file :)
