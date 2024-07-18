# Leslio McKeown
# 07/15/2024
# OOP-phrase-hunter-game (Project 3)

#from game import Game

class Phrase:
    def __init__(self, phrase):
        self.phrase = phrase.lower()

    def display(self, guesses):
        for letter in self.phrase:
            if letter in guesses or letter == ' ':
                print(f"{letter} ", end="")
            else:
                print("_ ", end="")
        print()  # Move to the next line after the display

    def check_guess(self, guess):
        return guess in self.phrase

    def check_complete(self, guesses):
        for letter in self.phrase:
            if letter not in guesses and letter.isalpha():
                return False
        return True

    def __str__(self):
        return self.phrase






