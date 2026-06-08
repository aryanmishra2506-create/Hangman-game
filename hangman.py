import random

# Hangman Game by Aryan

def hangman_game():
    words = ["python", "github", "programming", "calculator", "hangman"]
    word = random.choice(words)
    guessed = ["_"] * len(word)
    attempts = 6
    used_letters = []

    print("=== Welcome to Hangman ===")
    print("Word:", " ".join(guessed))

    while attempts > 0 and "_" in guessed:
        guess = input("Enter a letter: ").lower()

        if guess in used_letters:
            print("You already tried that letter.")
            continue

        used_letters.append(guess)

        if guess in word:
            for i in range(len(word)):
                if word[i] == guess:
                    guessed[i] = guess
            print("Correct! Word:", " ".join(guessed))
        else:
            attempts -= 1
            print("Wrong! Attempts left:", attempts)

    if "_" not in guessed:
        print("🎉 You won! The word was:", word)
    else:
        print("😢 You lost! The word was:", word)

hangman_game()
