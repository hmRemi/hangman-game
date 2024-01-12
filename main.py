from colorama import Fore
import random


def chose_word():
    words = open("words.txt", "r").read().splitlines()
    return random.choice(words)


def display_word(word, guessed_letters):
    display = ""

    for letter in word:
        if letter in guessed_letters:
            display += letter
        else:
            display += "_"
    return display


def hangman():
    print(f"{Fore.LIGHTBLACK_EX}[{Fore.WHITE}+{Fore.LIGHTBLACK_EX}]{Fore.WHITE} Welcome to Hangman!")

    max_attempts = int(input(f"{Fore.LIGHTBLACK_EX}[{Fore.WHITE}+{Fore.LIGHTBLACK_EX}]{Fore.WHITE} How many attempts do you want? "))
    guessed_letters = []
    word = chose_word()
    attempts = 0

    while attempts < max_attempts:
        current_display = display_word(word, guessed_letters)
        print(f"\n{Fore.LIGHTBLACK_EX}[{Fore.WHITE}+{Fore.LIGHTBLACK_EX}]{Fore.WHITE} Current word: {current_display}")

        if "_" not in current_display:
            print(f"{Fore.LIGHTBLACK_EX}[{Fore.WHITE}+{Fore.LIGHTBLACK_EX}]{Fore.WHITE} You guessed the word! The word was {word}.")
            break

        guess = input(f"{Fore.LIGHTBLACK_EX}[{Fore.WHITE}+{Fore.LIGHTBLACK_EX}]{Fore.WHITE} Guess a letter: ").lower()

        if guess.isalpha() and len(guess) == 1:
            if guess in guessed_letters:
                print(f"{Fore.LIGHTBLACK_EX}[{Fore.WHITE}+{Fore.LIGHTBLACK_EX}]{Fore.WHITE} You already guessed that letter!")
            elif guess in word:
                print(f"{Fore.LIGHTBLACK_EX}[{Fore.WHITE}+{Fore.LIGHTBLACK_EX}]{Fore.WHITE} You guessed a letter!")
                guessed_letters.append(guess)
            else:
                print(f"{Fore.LIGHTBLACK_EX}[{Fore.WHITE}+{Fore.LIGHTBLACK_EX}]{Fore.WHITE} You guessed an incorrect letter!")
                print(f"{Fore.LIGHTBLACK_EX}[{Fore.WHITE}+{Fore.LIGHTBLACK_EX}]{Fore.WHITE} You have {max_attempts - attempts} attempts left!")
                attempts += 1
                guessed_letters.append(guess)
        else:
            print(f"{Fore.LIGHTBLACK_EX}[{Fore.WHITE}+{Fore.LIGHTBLACK_EX}]{Fore.WHITE} You must guess a letter!")

    else:
        print(f"{Fore.LIGHTBLACK_EX}[{Fore.WHITE}+{Fore.LIGHTBLACK_EX}]{Fore.WHITE} You ran out of attempts! The word was {word}.")

if __name__ == "__main__":
    hangman()
