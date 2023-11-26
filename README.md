# Hangman
Hangman is a classic game in which a player thinks of a word and the other player tries to guess that word within a certain amount of attempts.

This is an implementation of the Hangman game, where the computer thinks of a word and the user tries to guess it. 

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

## How to play the game?
The game will start by hinting the number of characters in the word to be guessed.
Type a guess of your chosen single alphabetic character. The game will tell you if your guess was correct or not.
You will start with 5 lives and will lose a live for each incorrect attempt to guess a letter of the mistery word.
The game will terminate when you guess the word or run out of lives.

**Enjoy!**

## Usage example
Upon intialising the game you will be told the number of characters in the mistery word and a representation of the word with dashed lines:
```console
The mistery word has 5 characters
['_','_','_','_','_']

Enter a single letter:
```
If you enter 'a', for example, and the letter is in the mistery word, the game will tell you is a good guess and show you the position of the letter in the word. Then, if there are still letters to be guessed, the game will ask you for a new letter:

```console
Good guess, a is in the word.
['a','_','_','_','_']

Enter a single letter:
```

If you enter a letter that is not in the mistery word, again the game will tell you and you will lose a live. For example, if we typed 'k':
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
