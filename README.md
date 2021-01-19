# simple-py-hangman

###### CO1102 CW2 Project of Joe Groves and Sean Raisi. Originally written in November 2018.
-----------

A Python program which uses basic programming constructs and data types such as functions, strings, tuples and lists. As well as, file handling and exceptions.


## Problem (Taken directly from the problem sheet)
-----------

We would like to implement a simple two players game and then produce a histogram on the outcomes win and lose. The rules of the games are as follows:

1. Player 1, the computer must select a word at random from a list of available words that is provided in the file words.txt

2. Player 2, a human user aims a guessing the word selected by Player 1 by guessing its characters. They are given a certain number of guesses at the beginning.

3. Player 2 inputs their guess and Player 1 either:
  3a. reveals the letter if it exists in the secret word 
  3b. updates the number of guesses remaining
  
4. The game ends when either the user guesses the secret word, or the user runs out of guesses.

### Simple Python Hangman Report
-----------

A short report which describes functions: *is_secret_guessed(secret_word, letters_guessed)* and *first_game(secret_word)* and their respective test plans.
