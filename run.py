import random

"""
https://stackoverflow.com/questions/306400/how-can-i-randomly-select-an-item-from-a-list
"""

# hangman game function
def hangman():
    mylist = ["python", "javascript", "react", "github", "django", "bootstrap"]
    secretWord = random.choice(mylist)
    turns = 6
    lettersGuessed = ""
    valid_entry = set("abcdefghijklmnopqrstuvwxyz")

    while len(secretWord) > 0:
        main_word = ""

        for letter in secretWord:
            if letter in lettersGuessed:
                main_word = main_word + letter
            else:
                main_word = main_word + "_ "

        if main_word == secretWord:
            print(main_word)
            print("You won!!!!")
            break

        print("Pick a letter", main_word)
        guess = input()

        if guess in valid_entry:
            lettersGuessed = lettersGuessed + guess
        else:
            print("Enter a valid character")
            guess = input()
        if lettersGuessed in lettersGuessed:
            print('You tried that letter already')
            continue

        if guess not in secretWord:
            turns = turns - 1

            if turns == 6:
                print("6 turns left!")
                print("---------------")
            if turns == 5:
                print("5 turns left!")
                print("---------------")
                print("       O       ")
            if turns == 4:
                print("4 turns left!")
                print("---------------")
                print("       O       ")
                print("       |       ")
            if turns == 3:
                print("3 turns left!")
                print("---------------")
                print("       O       ")
                print("       |       ")
                print("      /        ")
            if turns == 2:
                print("2 turns left!")
                print("---------------")
                print("       O       ")
                print("       |       ")
                print("      / \      ")
            if turns == 1:
                print("1 turn left!")
                print("---------------")
                print("       O /     ")
                print("       |       ")
                print("      / \      ")
            if turns == 0:
                print("I'm sorry, you lose. Better luck next time!")
                print("---------------")
                print("     \ O /     ")
                print("       |       ")
                print("      / \      ")
            if turns == 0:
                print("Oh no!")
                print("---------------")
                print("       O_|     ")
                print("     / | \     ")
                print("      / \      ")
                print("I'm sorry, you lose. Better luck next time!")
                break


# Welcome message
print("Welcome to Hangman!")

# Rules
rules = """
The aim of the game is to correctly guess the hidden word...

Guess a letter to begin. If it's correct, the letter will be displayed.

If you guess incorrectly, you lose a life. You get a total of 6 lives.
-----------------------------------------------------------------------
"""
print(rules)

# Enter name
name = str(input("Enter your name: "))
print("\nWelcome, " + name)
print("\nTry to guess the secret word in less than 6 attempts\n")
hangman()