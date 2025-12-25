import random
from ascii_art import STAGES
# List of secret words
WORDS = ["python", "git", "github", "snowman", "meltdown"]

def get_random_word():
    """Selects a random word from the list."""
    return WORDS[random.randint(0, len(WORDS) - 1)]

def display_game_state(mistakes, secret_word, guessed_letters):
    # Display the snowman stage for the current number of mistakes.
    print(STAGES[mistakes])
    # Build a display version of the secret word.
    display_word = ""
    for letter in secret_word:
        if letter in guessed_letters:
            display_word += letter + " "
        else:
            display_word += "_ "
    print("Word: ", display_word.strip())
    print("\n")

def play_game():
    secret_word = get_random_word()
    guessed_letters = set()
    mistakes = 0
    max_mistakes = len(STAGES) - 1

    print("Welcome to Snowman Meltdown!")

    display_game_state(mistakes, secret_word, guessed_letters)
    print("Secret word selected: " + secret_word)  # for testing, later remove this line

    while mistakes < max_mistakes:
        display_game_state(mistakes, secret_word, guessed_letters)  # Zeige den aktuellen Zustand.

        # Benutzer nach einem Buchstaben fragen
        guess = input("Guess a letter: ").lower()

        print("You guessed:", guess)


        if len(guess) != 1 or not guess.isalpha():
            print("Please enter a valid single letter.")
            continue
        if guess in guessed_letters:
            print("You've already guessed that letter. Try again!")
            continue

        guessed_letters.add(guess)



if __name__ == "__main__":
    play_game()