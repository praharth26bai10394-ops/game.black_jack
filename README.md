# game.black_jack
# Blackjack Game

## Project Description

This project is a simple command-line Blackjack game developed using Python.

The project is divided into multiple Python modules to make the program easier to understand and manage. The game follows the basic rules of Blackjack where the player tries to get a score close to 21 without going over it.

The project was created as part of the Python Essentials course.

## Features

* Create and display playing cards.
* Create a deck containing standard playing cards.
* Deal cards to the player and dealer.
* Calculate the value of cards.
* Handle Aces as 1 or 11 depending on the score.
* Allow the player to choose whether to hit or stand.
* Calculate the final scores.
* Display the result of the game.
* Runs completely through the command line.

## Project Structure

```text
game.black_jack/
│
├── cards.py
├── deck.py
├── game.py
├── player.py
├── dealer.py
├── README.md
└── STATEMENT.md
```

### cards.py

Contains the `Card` class.

It stores:

* Suit of the card
* Rank of the card

It also contains the method used to display a card in the form:

```text
A of Spades
```

### deck.py

Contains the `Deck` class.

It creates a standard deck of 52 cards using the `Card` class.

### game.py

Contains the main game logic.

It includes:

* Card value calculation
* Score calculation
* Ace handling
* Drawing cards
* Player turn logic

### player.py

Contains the `Player` class.

It stores the player's name and cards and provides functions to display and add cards.

### dealer.py

Contains the `Dealer` class.

It stores the dealer's cards and provides functions related to dealing and displaying cards.

## Requirements

* Python 3.x
* No external libraries are required.

The project uses Python's built-in `random` module.

## How to Run

1. Install Python 3.x on your computer.
2. Download or clone this repository.
3. Open the project folder in a terminal.
4. Run the main game Python file using:

```bash
python game.py
```

The game will run in the command line.

## How to Play

1. The player receives cards.
2. The dealer receives cards.
3. The player's cards and score are displayed.
4. The player can choose to take another card or stop.
5. The score is calculated after each turn.
6. The dealer plays according to the game logic.
7. The final scores are compared.
8. The result of the game is displayed.

## Concepts Used

This project uses concepts learned in Python Essentials, including:

* Variables
* Input and output
* Conditional statements
* `if`, `elif`, and `else`
* Loops
* Functions
* Classes and objects
* Lists
* Importing modules
* Random selection
* Basic object-oriented programming

