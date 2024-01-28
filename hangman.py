'''
Hangman is a classic game in which a player thinks of a word and the
other player tries to guess that word within a certain amount of 
attempts.
This is an implementation of the Hangman game, where the computer 
chooses of a word and the user tries to guess it.
It starts with a default number of lives defined by the variable 
num_lives and a random word from the variable word_list.
'''
import random


class Hangman:
    '''
    Parameters:
    ----------
    word_list: list
        List of words to be used in the game
    num_lives: int
        Number of lives the player has
    
    Attributes:
    ----------
    word: str
        The word to be guessed picked randomly from the word_list
    word_guessed: list
        A list of the letters of the word, with '_' for each letter not yet guessed
        For example, if the word is 'apple', the word_guessed list would be:
        ['_', '_', '_', '_', '_']
        If the player guesses 'a', the list would be:
        ['a', '_', '_', '_', '_']
    num_letters: int
        The number of UNIQUE letters in the word that have not been guessed yet
    num_lives: int
        The number of lives the player has
    list_letters: list
        A list of the letters that have already been tried

    Methods:
    -------
    check_letter(letter)
        Checks if the letter is in the word.
    ask_letter()
        Asks the user for a letter.
    '''  
    def __init__(self, word_list, num_lives=5):
        #Initialise the attributes
        self.word=random.choice(word_list)
        self.word_guessed=['_' for count in range(len(self.word))]
        self.num_letters=len(set(self.word)) #int of the letters to be guessed
        self.num_lives=num_lives
        self.list_letters=[]

        #Print messages upon initialization:
        print(f"The mistery word has {len(self.word)} characters")
        print(f"{self.word_guessed}\n")

    def check_letter(self, guess) -> None:
        '''
        Checks if the letter is in the word.
        If it is, it replaces the '_' in the word_guessed list with the letter.
        If it is not, it reduces the number of lives by 1.

        Parameters:
        ----------
        guess: str
            The letter to be checked

        '''
        guess=guess.lower() #converts the letter to lowercase

        #Check if the letter is in the word:
        if guess in self.word:
            print(f'Good guess, {guess} is in the word.')

            #If the letter is in the word, 
            #replace the '_' in the word_guessed list with the letter:
            for index, character in enumerate(self.word):
                if character == guess:
                    self.word_guessed[index]=guess
            
            self.num_letters -=1 
            print(f"{self.word_guessed}\n") #show the current status of the game
        else:
            print(f'Sorry, {guess} is not in the word. Try again.')

            #If the letter is not in the word, reduce the number of lives by 1:
            self.num_lives -=1 
            print(f"You have {self.num_lives} lives left.\n")

    def ask_letter(self):
        '''
        Asks the user for a letter and checks two things:
        1. If the letter has already been tried
        2. If the character is a single character
        If it passes both checks, it calls the check_letter method.
        '''
        guess= input('Enter a single letter: ')

        if guess in self.list_letters:
            print(f"{guess} was already tried")
        elif len(guess)==1 and guess.isalpha()==True:
            self.check_letter(guess)
            self.list_letters.append(guess)
        else:
            print('Invalid letter. Please, enter a single alphabetical character.')


def play_game(word_list, num_lives):
    game = Hangman(word_list, num_lives)

    #Iteratively ask the user for a letter until 
    #the user guesses the word or runs out of lives:
    while True:
        if game.num_lives == 0:
            print(f"You lost! The word was {game.word}")
            break #terminate the game
        elif game.num_letters > 0: #if there are letters to be guessed 
            game.ask_letter()
        else:
            print('Congratulations. You won the game!')
            break #terminate the game

if __name__ == '__main__':
    word_list = ['apple', 'banana', 'orange', 'pear', 'strawberry', 'watermelon']
    num_lives = 5
    play_game(word_list, num_lives)
# %%
