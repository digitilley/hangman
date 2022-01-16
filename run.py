import gspread
from google.oauth2.service_account import Credentials

SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
    ]

CREDS = Credentials.from_service_account_file('creds.json')
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open('random_word')

words = SHEET.worksheet('words')

data = words.get_all_values()
print(data)

#Welcome message
print("Welcome to Hangman!")

#Rules
"""
used this article to help with rules section:
https://stackoverflow.com/questions/34980251/how-to-print-multiple-lines-of-text-with-python
"""
rules = """
The aim of the game is to correctly guess the random word...

Guess a letter to begin. If it's correct, the letter will be displayed.

If you guess incorrectly, you will lose 1 life. You get a total of 6 lives.
"""
print(rules)

#Player name
name = str(input("Enter your name: "))

#Good luck message
print("\nGood luck, "+ name)

#Random Word

