# Hangman - a python game

<p align="center">
  <img src="https://raw.githubusercontent.com/DGValero/hangman/main/Hangman_cover_image.jpg" alt="Hangman_cover_image"/>
</p>

In the classic children's game of Hangman, a player's objective is to identify a hidden word of which only the number of letters is originally revealed. In each round, the player guesses a letter of the alphabet: if it's present in the word, all instances are revealed; otherwise, one of the hangman's body parts is drawn in on a gibbet. The game ends in a win if the word is entirely revealed by correct guesses, and ends in loss if the hangman's body is completely revealed instead. To assist the player, a visible record of all guessed letters is maintained.

This is an implementation of the Hangman game, where the computer chooses a secret word and the user tries to guess it. 

## How to play the game?
To win the game you will have to guess the mystery word, before running out of lives.
The game will start by hinting the number of characters in the word to be guessed.
The user will then be asked to type a guess of a chosen single alphabetic character. If your guess was in the mystery word, the letter/s guessed will be shown on the screen. However, if you were incorrect you will lose a live. You will start with 5 lives and will lose the game if you run out of lives.

**Enjoy the game!**

## Usage example
Upon initialising the game you will be told the number of characters in the mystery word and a representation of the word with dashed lines:
```console
The mystery word has 5 characters
['_','_','_','_','_']

Enter a single letter:
```
If you enter 'a', for example, and the letter is in the mystery word, the game will tell you is a good guess and show you the position of the letter in the word. Then, if there are still letters to be guessed, the game will ask you for a new letter:

```console
Good guess, a is in the word.
['a','_','_','_','_']

Enter a single letter:
```

If you enter a letter that is not in the mystery word, again the game will tell you and you will lose a live. For example, if we typed 'k':
```console
Sorry, k is not in the word. Try again.
You have 4 lives left.

Enter a single letter:
```
If you guessed all the letters in the word before losing all your lives you will be greeted with the following message and the game will terminate:
```console
Good guess, e is in the word.
['a','p','p','l','e']

Congratulations. You won the game!
```
## Tailoring the code

You may want to tailor the game to play with the words you choose and you may also want to modify the number of lives you are given at the beginning. To modify these parameters, you will need to change the following variables in the `hangman.py` python code: `word_list` and `num_lives`:

`word_list`: this variable is defined in **line 125** of the code and it contains the list of mystery words to be used in the game. Each time you run the game, a word from the list will be chosen at random. This parameter must be stored as a python list. By default the list of words is shown below but the list can be modified to suit your taste.

```python
word_list = ['apple', 'banana', 'orange', 'pear', 'strawberry', 'watermelon']
```

`num_lives`: this variable is defined in **line 126** of the code and it is defined as an integer of the number of lives the player has. By default you will start the game with 5 lives:

```python
num_lives = 5
```

## Programming language
Python 3.6

## Dependencies
- *Python 3.6*
- Python's *random* module
- *git* to clone the repo

## Installation instructions
### Initialising the repository in an existing directory:
First initialise git bash. Then you will need to navigate to the folder directory where you would like to save the game. For example in Windows:
> cd C:/Users/user/my_games

To get a copy of this repository, you can do so with the following command:
> git clone https://github.com/DGValero/hangman.git

### How to initiate the hangman game?
Navigate to the root of the repository. Following the example above, it would be:
> cd C:/Users/user/my_games/hangman

and run **hangman.py** from your terminal:

> python hangman.py