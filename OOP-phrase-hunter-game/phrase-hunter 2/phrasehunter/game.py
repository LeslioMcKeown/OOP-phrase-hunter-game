# Leslio McKeown
# 07/15/2024
# OOP-phrase-hunter-game (Project 3)

import random
from phrase import Phrase


class Game:
    def __init__(self):
        self.missed = 0
        self.phrases = self.create_phrases()
        self.active_phrase = self.get_random_phrase()
        self.guesses = []

    def create_phrases(self):
        return [
            Phrase('Hello world'),
            Phrase('There is no trying'),
            Phrase('May the force be with you'),
            Phrase('You have to see the matrix for yourself'),
            Phrase('Life is like a box of chocolates')
        ]

    def get_random_phrase(self):
        return random.choice(self.phrases)

    def welcome(self):
        print("============================")
        print("Welcome to Phrase Hunter")
        print("============================")

    def start(self):
        self.welcome()  # Call the welcome method

        while self.missed < 5 and not self.is_phrase_revealed():
            print(f"Number missed: {self.missed}")  # Print the number of missed guesses
            self.active_phrase.display(self.guesses)  # Call the display method on active_phrase

            # Get the user’s guess
            user_guess = self.get_guess()
            #print(user_guess)

            # Add the user's guess to the guesses list
            self.guesses.append(user_guess)

            # Check if the guess is correct
            if not self.active_phrase.check_guess(user_guess):
                self.missed += 1  # Increase the number of missed guesses if incorrect

            # Call the display method again to show the updated phrase
            self.active_phrase.display(self.guesses)

        # After the loop ends
        self.end_game()


        while self.missed < 5 and not self.active_phrase.check_complete(self.guesses):
            print(f"Number missed: {self.missed}")  # Print the number of missed guesses
            self.active_phrase.display(self.guesses)  # Call the display method on active_phrase

        # Get the user’s guess
        user_guess = self.get_guess()


        # Add the user's guess to the guesses list
        self.guesses.append(user_guess)

        if self.active_phrase.check_guess(user_guess):
            print("You got one!")
        else:
            print("Oof wrong letter!")
            self.missed += 1  # Increase the number of missed guesses if incorrect

        # Call the display method again to show the updated phrase
        self.active_phrase.display(self.guesses)

        # After the loop ends
        self.end_game()

    def get_guess(self):
        guess = input("Enter a letter: ").lower()
        return guess

    def is_phrase_revealed(self):
        # Check if all letters in the phrase have been guessed
        for letter in self.active_phrase.phrase:
            if letter not in self.guesses and letter.isalpha():
                return False
        return True

    def end_game(self):
        if self.active_phrase.check_complete(self.guesses):
            print("Congratulations! You've won!")
        else:
            print(f"Sorry, you've lost. The phrase was: {self.active_phrase.phrase}")


