# Blackjack Game. Project Statement

## 1. Project

# Blackjack Game Using Python

---

## 2. Problem Statement

Blackjack is a card game in which a player competes against a dealer.

The main objective of the game is to obtain a card score as to 21 as possible without exceeding 21.

The purpose of this project is to develop a command-line based Blackjack game using Python. The project will simulate the flow of a blackjack game between one human player and a computer-controlled dealer.

The project will. Manage a standard deck of 52 playing cards shuffle the deck, deal cards to the player and dealer calculate their scores and determine the result of each round.

The project is also intended to demonstrate the application of python programming concepts learned during the course. These concepts include variables, lists, loops, conditional statements, functions, modules, randomization, user input and basic error handling.

Of putting all the program logic into one large Python file the project will divide the program into multiple modules. Each module will perform a responsibility making the project easier to understand

test maintain and modify.

The project will provide an interactive command-line experience where the user can make decisions during the game and receive the result after the round is completed.

---

## 3. Project Objectives

The main objectives of this project are:

1. To develop a Blackjack game using Python.

2. To apply Python programming concepts learned in the course to a

project.

3. To create a 52-card deck programmatically.

4. To implement card shuffling and card dealing.

5. To calculate Blackjack scores correctly.

6. To implement the Hit and Stand decisions for the player.

7. To implement the predefined playing rules for the dealer.

8. To determine whether the player wins. Draws against the dealer.

9. To organize the project into meaningful Python modules.

10. To practice programming and separation of responsibilities.

11. To include input validation and error handling.

12. To test parts of the program before integrating them into the

complete game.

13. To maintain the project using Git and GitHub version control.

14. To document the design, implementation, testing and learning outcomes

of the project.

---

## 4. Scope of the Project

### 4.1 Included in the Scope

The project will include:

- Representation of playing cards.

- Creation of a 52-card deck.

- Four card suits:

Hearts

Diamonds

Clubs

Spades

- Thirteen card ranks:

2 To 10

Jack

Queen

King

Ace

- Shuffling of the deck.

- Dealing cards from the deck.

- Maintaining the players hand.

- Maintaining the dealers hand.

- Calculating the players score.

- Calculating the dealers score.

- Handling the scoring rule of the Ace.

- Player choice between Hit and Stand.

- Dealer decision according to the implemented game rule.

- Detection of Blackjack and scores exceeding 21.

- Comparison of player and dealer scores.

- Displaying the result of a round.

- Option to play another round.

- Basic input validation.

- testing of important program components.

### 4.2 Outside the Scope

This project will not include :

- Real-money betting.

- gambling.

- Multiplayer functionality.

- Online accounts or user registration.

- Online leaderboards.

- Internet-based gameplay.

- A graphical user interface.

- Mobile application functionality.

- multiplayer servers.

The project will focus on creating a functional and understandable

command-line Blackjack simulation using Python.

---

## 5. Target Users

The project is primarily intended for the following users:

### 5.1 Python Beginners

Students who are learning Python can use the project to understand how

basic Python concepts can be combined to create an application.

### 5.2 Students

Students can use the project as an example of applying programming concepts

such as functions, lists, loops, conditional statements, modules and

randomization.

### 5.3 Beginner Programmers

Beginner programmers can study the structure of the project and

understand how a larger program can be divided into smaller components.

### 5.4 Casual Users

Users who want to play a command-line version of Blackjack can use

the application without requiring a graphical interface or external

software.

---

## 6. High-Level Features

### 6.1 Card Management

The project will contain a module for representing individual

playing cards.

Each card will contain information such as:

- Suit

- Rank

For example:

- 7 of Hearts

- King of Spades

- Ace of Diamonds

---

### 6.2 Deck Management

The project will create a deck containing 52 cards.

The deck module will be responsible for:

- Creating the cards.

- Storing the cards.

- Shuffling the cards.

- Dealing cards.

- Removing dealt cards from the deck.

The deck will contain four suits and thirteen ranks resulting in:

4 × 13 = 52 cards

---

### 6.3 Player Management

The player module will manage the players hand.

It will be responsible for:

- Storing cards received by the player.

- Adding cards to the players hand.

- Calculating the players score.

- Displaying the players cards.

- Supporting the players Hit or Stand decision.

---

### 6.4 Dealer Management

The dealer module will manage the computer-controlled dealer.

It will be responsible for:

- Storing the dealers cards.

- Adding cards to the dealers hand.

- Calculating the dealers score.

- Following the dealers predefined decision rule.

- Stopping when the dealer reaches the score.

---

### 6.5 Score Calculation

The game will calculate the score of the cards in a hand according to

Blackjack rules.

Number cards will use their values.

For example:

2 = 2

5 = 5

10 = 10

Face cards will have a value of 10:

Jack = 10

Queen = 10

King = 10

The Ace will require handling because it can contribute either

1 or 11 depending on the total hand score.

The program will therefore check the hand. Select the appropriate Ace

value to avoid exceeding 21 whenever possible.

---

### 6.6 Hit and Stand

During the players turn the player will be able to choose between:

### Hit

The player receives another card.

The players score is then recalculated.

If the score becomes greater than 21 the player loses the round.

### Stand

The player stops taking cards.

The turn then moves to the dealer.

---

### 6.7 Dealer Decision

After the player completes their turn the dealer will play according to

the predefined rule implemented in the program.

The dealer will continue taking cards while the dealers score's below

the required threshold.

Once the dealer reaches the required threshold the dealer will stop taking

cards.

---

### 6.8 Winner Determination

After both the player and dealer have completed their turns the game will

compare their scores.

The program will determine the result based on the implemented

Blackjack rules, such as:

- Player wins.

- Dealer wins.

- Draw.

- Player busts.

- Dealer busts.

- Blackjack where applicable.

The result will be displayed clearly to the user.

---

### 6.9 Multiple Rounds

After a round is completed the program can allow the user to decide

whether to start another round.

This allows the user to continue playing without restarting the Python

program

---

### 6.10 Input Validation

The project will validate user inputs.

For example when the program asks the player to choose between Hit and

Stand it will check whether the entered choice is valid.

Invalid input will result in a message instead of causing the

program to terminate unexpectedly.

---

### 6.11 Testing

The project will include testing for parts of the program.

Testing will include checking:

- Card creation.

- Deck creation.

- Number of cards in a deck.

- Shuffling.

- Dealing cards.

- Score calculation.

- Ace handling.

- Player decisions.

- Dealer decisions.

- Winner determination.

- Invalid input handling.

---

## 7. Proposed Module Structure

The project will be divided into Python files so that each module

has a clear responsibility.

### cards.py

Responsible, for representing a playing card.

### deck.py

Responsible for creating, storing, shuffling and dealing cards.

### player.py

Responsible for maintaining the players hand and calculating the players score.

### dealer.py

Responsible for maintaining the dealers hand and implementing the dealers decision logic.

### game.py

Responsible for controlling the Blackjack game flow.

### utils.py

Responsible for reusable helper functions such as input validation and displaying information.

### main.py

Responsible for starting the application and providing the entry point for the user.

### tests.py

Responsible for performing tests on important project components.

---

## 8. Expected Input

The main input will be provided by the user through the command line.

Examples include:

- Choosing whether to start a game.

- Choosing Hit or Stand.

- Choosing whether to play another round.

The program will validate these inputs wherever necessary.

---

## 9. Expected Output

The program will display information such as:

- Players cards.

- Dealers cards.

- Players score.

- Dealers score when appropriate.

- Cards received after choosing Hit.

- Final dealer hand.

- Final scores.

- Result of the round.

- Messages for inputs.

- Option to play another round.

---

## 10. Basic Game Workflow

The overall workflow of the project will be:

1. Start the program.

2. Initialize a deck.

3.. Shuffle the deck.

4. Deal the cards to the player and dealer.

5. Calculate the scores.

6. Display the cards and scores.

7. Ask the player whether to Hit or Stand.

8. If the player chooses Hit deal another card. Calculate the score again.

9. Continue the players turn until the player chooses Stand or exceeds 21.

10. If the player has not exceeded 21 start the dealers turn.

11. The dealer follows the implemented dealer rule.

12. Compare the scores.

13. Display the result.

14. Ask the user whether another round should be played.

15. Start another round. Terminate the program.

---

## 11. Technical Approach

The project will be implemented using Python.

The implementation will use:

- Python classes where appropriate.

- Functions for operations.

- Lists for storing cards.

- Loops for repeated operations.

- Conditional statements for game decisions.

- The random module for shuffling.

- Separate Python modules for different responsibilities.

- Basic validation for user input.

- Git and GitHub for version control.

No external Python libraries will be required for the version of the project.

---

## 12. Error Handling Approach

The project will attempt to handle input and game-related errors.

Examples include:

- Invalid Hit/Stand input.

- user choices.

- Attempting to deal when the deck has no cards.

- Invalid game-state conditions.

The program should provide a message to the user instead of terminating unexpectedly whenever practical.

---

## 13. Expected Outcome

At the completion of the project the user should be able to run the Python program from the command line and play a Blackjack round against the computer-controlled dealer.

The project should demonstrate that Python programming concepts can be combined into an application with a clear workflow.

The final project should also provide organized source code, documentation, testing information and a GitHub repository containing the development history.

---

## 14. Future Enhancements

The following features may be considered for versions:

- Graphical user interface.

- Multiple players.

- Betting system using virtual points only.

- Score or statistics tracking.

- Different difficulty settings.

- detailed game statistics.

- Improved card display.

- Additional automated tests.

- Persistent game statistics.

These enhancements are outside the scope of the version and may be considered after the basic Blackjack game has been completed.

---

## 15. Project Limitations

The initial version of the project will have some limitations.

The game will be command-line based. Will not provide graphical visualization.

The game will focus on one player and one computer-controlled dealer.

The project will not use a database or internet-based multiplayer system.

The implementation will prioritize simplicity and understanding of Python programming concepts because the project is intended as a student-level application.

---

## 16.

The Blackjack Game project is designed as a Python application that demonstrates the use of programming fundamentals in a complete project.

By dividing the application into modules for cards, deck management, players, dealers, game control, utilities and testing the project aims to maintain a clear and understandable structure.

The project will provide a command-line Blackjack experience while also demonstrating concepts such, as modular programming, data management, conditional logic, loops, functions, randomization, validation, testing and version control.