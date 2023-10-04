import random

class Hangman:
    def __init__(self, word_list, num_lives=10):
        '''
        Initialise the variables
        '''
        self.word_list=word_list
        self.num_lives=num_lives
        self.num_letters=len(set(word)) #int of the letters to be guessed

    def check_guess(self, guess):
        '''
        This method takes the letter introduced in the game and checks if it is in the word.
        Substracts a life if you get the wrong letter.
        It also puts the letters guessed in word_guessed and prints the list of letters guessed so far.
        '''
        guess=guess.lower()
        if guess in word:
            print(f'Good guess, {guess} is in the word.')
            i=0
            for letter in word:
                if guess == letter:
                    word_guessed[i]=guess
                i +=1
            self.num_letters -=1 #one less letter to be guessed!
            print(word_guessed) #show the list of letters
        else:
            print(f'Sorry, {guess} is not in the word. Try again.')
            self.num_lives -=1
            print(f"You have {self.num_lives} lives left.")

    def ask_for_input(self):
        '''
        This method asks for input and check if the input is valid.
        If so, it calls the check_guss method
        '''
        guess= input('Enter a single letter: ')

        if guess in list_of_guesses:
            print("You already tried that letter!")
        elif len(guess)==1 and guess.isalpha()==True:
            self.check_guess(guess)
            list_of_guesses.append(guess)
        else:
            print('Invalid letter. Please, enter a single alphabetical character.')

#Initialise some variables:

word_list=['melon', 'pineapple', 'peach', 'banana', 'strawberries'] 

word = random.choice(word_list) #Chooses a word of the list word_list to be guessed for the current game
word_guessed=[]
list_of_guesses=[] #A list of the guesses that have already been tried. Set this to an empty list initially


#Creates list of the guesses with '_'.
for count in range(len(word)):
    word_guessed.append('_')

#Main function of the game
def play_game(word_list):
    num_lives=5 #Initial number of lives
    game = Hangman(word_list, num_lives) #Create instance of the class
    
    while True:
        if game.num_lives == 0:
            print('you lost')
            break #terminate the game
        elif game.num_letters > 0: #if there are letters to be guessed 
            game.ask_for_input()
        else:
            print('Congratulations. You won the game!')
            break #terminate the game

play_game(word_list)

