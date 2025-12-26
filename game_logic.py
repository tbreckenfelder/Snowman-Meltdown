import random
from ascii_art import STAGES
import string
# List of secret words
WORDS = ["python", "git", "github", "snowman", "meltdown"]

def get_random_word():
    """Selects a random word from the list."""
    return random.choice(WORDS)

def display_game_state(mistakes, secret_word, guessed_letters, remaining_errors):
    print(STAGES[mistakes])

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

    print("Willkommen zu: Snowman Meltdown!")

    display_game_state(mistakes, secret_word, guessed_letters, max_mistakes)
    print("Secret word gewählt: " + secret_word)  # for testing, later remove this line

    while mistakes <= max_mistakes:
        remaining_errors = max_mistakes - mistakes
        display_game_state(mistakes, secret_word, guessed_letters, max_mistakes)  # Zeige den aktuellen Zustand.
        print(f"Verfügbare Falscheingaben: {remaining_errors}")

        guess = input("Gib einen Buchstaben ein: ").lower()
        print("Du hast eingeben:", guess)

        if len(guess) != 1 or not guess.isalpha():
            print("Bitte gib einen gültigen Buchstaben ein.")
            continue
        if guess in guessed_letters:
            print("Du hast den Buchstaben schon eingeben. Versuche es nochmal!")
            continue

        guessed_letters.add(guess)

        if guess in secret_word:
            print(f"Super, der Buchstabe '{guess}' ist innerhalb des Wortes.")
        else:
            print(f"Falsch! der Buchstabe '{guess}' ist nicht innerhalb des Wortes.")
            mistakes += 1

        if all(letter in guessed_letters for letter in secret_word):
            print(f"==> Glückwunsch, du hast den Schneemann gerettet! <==")
            break

        if mistakes == max_mistakes:
            print(STAGES[mistakes])
            print("Du hast die maximale Fehleranzahl erreicht.")


if __name__ == "__main__":
    play_game()