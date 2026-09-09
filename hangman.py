"""
CodeAlpha Internship — Task 1: Hangman Game
Author: Aaron Baidoo (RoniKid)
Description: A text-based Hangman game. Player guesses a hidden word
             one letter at a time. 6 wrong guesses allowed.
"""

import random

# ── Word list ──────────────────────────────────────────────────────────────────
WORDS = ["python", "hangman", "coding", "laptop", "terminal"]

# ── ASCII art stages (index 0 = fresh gallows, index 6 = full hang) ───────────
HANGMAN_STAGES = [
    """
       -----
       |   |
           |
           |
           |
           |
    =========""",
    """
       -----
       |   |
       O   |
           |
           |
           |
    =========""",
    """
       -----
       |   |
       O   |
       |   |
           |
           |
    =========""",
    """
       -----
       |   |
       O   |
      /|   |
           |
           |
    =========""",
    """
       -----
       |   |
       O   |
      /|\\  |
           |
           |
    =========""",
    """
       -----
       |   |
       O   |
      /|\\  |
      /    |
           |
    =========""",
    """
       -----
       |   |
       O   |
      /|\\  |
      / \\  |
           |
    ========="""
]


def display_state(wrong_guesses, guessed_letters, secret_word):
    """Print the current hangman stage, the word progress, and used letters."""
    print(HANGMAN_STAGES[len(wrong_guesses)])
    print()

    # Show correctly placed letters and blanks
    word_display = " ".join(
        letter if letter in guessed_letters else "_"
        for letter in secret_word
    )
    print(f"  Word: {word_display}")
    print(f"  Wrong guesses ({len(wrong_guesses)}/6): {', '.join(sorted(wrong_guesses)) or 'none'}")
    print()


def get_player_guess(guessed_letters):
    """Prompt the player for a valid, unused single letter."""
    while True:
        guess = input("  Guess a letter: ").strip().lower()

        if len(guess) != 1:
            print("  ✗  Please enter exactly one letter.")
        elif not guess.isalpha():
            print("  ✗  Letters only, no numbers or symbols.")
        elif guess in guessed_letters:
            print(f"  ✗  You already guessed '{guess}'. Try another.")
        else:
            return guess


def play_hangman():
    """Run one full round of Hangman."""
    secret_word = random.choice(WORDS)
    guessed_letters = set()   # all letters the player has tried
    wrong_guesses = set()     # only the incorrect ones
    max_wrong = 6

    print("\n" + "=" * 40)
    print("       Welcome to Hangman!")
    print("=" * 40)
    print(f"  The word has {len(secret_word)} letters. Good luck!\n")

    while True:
        display_state(wrong_guesses, guessed_letters, secret_word)

        # ── Win check ──────────────────────────────────────────────────────────
        if all(letter in guessed_letters for letter in secret_word):
            print(f"  🎉  You won! The word was '{secret_word}'.")
            break

        # ── Loss check ─────────────────────────────────────────────────────────
        if len(wrong_guesses) >= max_wrong:
            print(HANGMAN_STAGES[max_wrong])
            print(f"\n  💀  Game over. The word was '{secret_word}'.")
            break

        # ── Player turn ────────────────────────────────────────────────────────
        guess = get_player_guess(guessed_letters)
        guessed_letters.add(guess)

        if guess in secret_word:
            print(f"  ✓  '{guess}' is in the word!\n")
        else:
            wrong_guesses.add(guess)
            remaining = max_wrong - len(wrong_guesses)
            print(f"  ✗  '{guess}' is not in the word. {remaining} guess(es) left.\n")


def main():
    while True:
        play_hangman()
        again = input("\n  Play again? (y/n): ").strip().lower()
        if again != "y":
            print("\n  Thanks for playing. Goodbye!\n")
            break


if __name__ == "__main__":
    main()
