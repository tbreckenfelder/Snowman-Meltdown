import random
from ascii_art import STAGES

# List of secret words
WORDS = ["python", "git", "github", "snowman", "meltdown"]

def get_random_word():
    """Selects a random word from the list."""
    return random.choice(WORDS)

def display_game_state(mistakes, secret_word, guessed_letters):
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

    while mistakes <= max_mistakes:
        remaining_errors = max_mistakes - mistakes
        display_game_state(mistakes, secret_word, guessed_letters)  # Zeige den aktuellen Zustand.
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
            print("==> Glückwunsch, du hast den Schneemann gerettet! <==")
            print(f"Das geheime Wort lautet: '{secret_word}'")
            print("\n")
            break

    if mistakes >= max_mistakes:
        print("Du hast die maximale Fehleranzahl erreicht.")
        print("==> Leider hast du den Schneemann nicht gerettet. <==")
        print("\n")

    replay = input("Möchtest du noch einmal spielen? (j/n): ").lower()

    if replay == "j":
        play_game()
    else:
        print("Schade, wir sehen uns ein anderes Mal!")

if __name__ == "__main__":
    play_game()