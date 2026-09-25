# Blackjack Game

## Project Description

This project is a command-line Blackjack game built using Python

The project is separated into multiple Python modules to make the program easier to understand and manage. The game follows the rules of Blackjack where the player tries to get a score close to 21 without going over it

The project was made as part of the Python Essentials course

## Features

* Create and show playing cards

* Create a deck containing standard playing cards

* Deal cards to the player and dealer

* Calculate the value of cards

* Handle Aces, as 1 or 11 based on the score

* Let the player decide whether to hit or stand

* Calculate the scores

* Show the result of the game

* Runs completely through the command line

## Project Structure

game.black_jack:

1) cards.py

2) deck.py

3) game.py

4) player.py

5) dealer.py

6) README.md

7) STATEMENT.md

### cards.py

Contains the 'Card' class

It stores:

1) Suit of the card

2) Rank of the card

It also contains the method used to show a card in the form:

A of Spades

### deck.py

Contains the 'Deck' class

It creates a deck of 52 cards using the 'Card' class

### game.py

Contains the main game logic

It includes:

1) Card value calculation

2) Score calculation

3) Ace handling

4) Drawing cards

5) Player turn logic

### player.py

Contains the 'Player' class

It stores the players name and cards and provides functions to show and add cards

### dealer.py

Contains the 'Dealer' class

It stores the dealers cards and provides functions related to dealing and showing cards

## Requirements

* Python program

* No external libraries are needed

The project uses Pythons built-in 'random' module

## How to Run

1) Install Python on your computer

2) Download or clone this repository

3) Open the project folder in a terminal

4) Run the main game Python file using:

'''bash

python game.py

'''

The game will run in the command line

## How to Play

1) The player gets cards

2) The dealer gets cards

3) The players cards and score are shown

4) The player can choose to take another card or stop

5) The score is calculated after each turn

6) The dealer plays according to the game logic

7) The final scores are compared

8) The result of the game is shown

## Concepts Used

This project uses concepts learned in Python Essentials including:

--> Variables

--> Input and output

--> statements

--> 'if' 'elif' and 'else'

--> Loops

--> Functions

--> Classes and objects

--> Lists

--> Importing modules

--> Random selection

--> Basic object-oriented programming