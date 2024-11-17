import random

def hangman():
    words = ["python", "hangman", "developer", "code", "programming"]
    word_to_guess = random.choice(words)
    guessed_word = ["_"] * len(word_to_guess)
    attempts = 6
    guessed_letters = []

    print("Welcome to Hangman!")
    print("Guess the word: " + " ".join(guessed_word))

    while attempts > 0:
        guess = input(f"\nGuess a letter (Attempts left: {attempts}): ").lower()

        if guess in guessed_letters:
            print(f"You already guessed '{guess}'")
        elif guess in word_to_guess:
            print(f"Good guess! '{guess}' is in the word.")
            guessed_letters.append(guess)
            for i in range(len(word_to_guess)):
                if word_to_guess[i] == guess:
                    guessed_word[i] = guess
        else:
            print(f"Sorry, '{guess}' is not in the word.")
            guessed_letters.append(guess)
            attempts -= 1

        print("Current word: " + " ".join(guessed_word))

        if "_" not in guessed_word:
            print("\nCongratulations! You've guessed the word!")
            break

    if attempts == 0:
        print(f"\nGame over! The word was '{word_to_guess}'.")

# Run the game
if __name__ == "__main__":
    hangman()