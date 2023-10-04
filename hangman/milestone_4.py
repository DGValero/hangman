import random

class Hangman:
    def __init__(self, word_list, num_lives=10):
        self.word_list=word_list
        self.num_lives=num_lives
        

    def check_guess(self, guess):
        guess=guess.lower()
        num_letters=len(set(word))
        if guess in word:
            print(f'Good guess, {guess} is in the word.')
            i=0
            for letter in word:
                if guess == letter:
                    word_guessed[i]=guess
                i +=1
            num_letters -=1
            print(word_guessed)
        else:
            print(f'Sorry, {guess} is not in the word. Try again.')
            self.num_lives -=1
            print(f"You have {self.num_lives} lives left.")

    def ask_for_input(self):
        '''
        This method asks for input and check if the input is valid. If so, it calls the check_guss method
        '''
        while True:
            guess= input('Enter a single letter: ')

            if guess in list_of_guesses:
                print("You already tried that letter!")
            elif len(guess)==1 and guess.isalpha()==True:
                self.check_guess(guess)
                list_of_guesses.append(guess)
            else:
                print('Invalid letter. Please, enter a single alphabetical character.')
        
        self.check_guess(guess)


word_list=['melon', 'pineapple', 'peach', 'banana', 'strawberries']

word = random.choice(word_list) #Chooses a word to be guessed for the current game

word_guessed=[]
num_lives=10 #The number of lives the player has at the start of the game. 
list_of_guesses=[] #A list of the guesses that have already been tried. Set this to an empty list initially

for count in range(len(word)):
    word_guessed.append('_')

my_game = Hangman(word_list)
my_game.ask_for_input()


