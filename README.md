# Blackjack Game

## Introduction
Welcome to my Blackjack game! This is a simple text-based implementation of the popular casino card game. The objective of the game is to get a hand value as close to 21 as possible without exceeding it.

## Rules
1. The game is played with a standard deck of 52 cards.
2. Each card has a value: numbered cards are worth their face value, face cards (J, Q, K) are worth 10, and the Ace can be worth either 1 or 11.
3. At the start of the game, the player and the dealer are each dealt two cards.
4. The player can choose to "hit" (draw another card) or "stand" (keep the current hand).
5. If the player's hand value exceeds 21, they "bust" and lose the game.
6. After the player's turn, the dealer reveals their second card and continues to draw cards until their hand value is 17 or higher.
7. If the dealer's hand value exceeds 21, they "bust" and the player wins.
8. If neither the player nor the dealer busts, the one with the hand value closest to 21 wins.
9. In case of a tie, it's a "push" and the game ends in a draw.

## Setup Instructions
To play the Blackjack game, follow these steps:

1. Clone this repository to your local machine.
2. Navigate to the project directory in your terminal.
3. Make sure you have Python installed on your machine.
4. Run the following command to start the game:
  ```
  python blackjack.py
  ```
5. Follow the on-screen instructions to play the game.

That's it! Enjoy playing Blackjack in the terminal!

## Reflections
This is my second Python project, and it was more complex compared to my first project, Rock Paper Scissors. In this Blackjack game, I had to work with additional data structures such as tuples and utilize for loops and conditional logic.

The use of `tuples` allowed me to represent the deck of cards and their values. I could easily access and manipulate the cards using indexing and slicing operations.

The `for` loops were essential for iterating over the cards in the deck and calculating the hand values. I could iterate over the player's and dealer's hands to determine the total value and make decisions based on the game rules.

Conditional logic played a crucial role in implementing the game rules. I used `if` statements to check for conditions such as busting, winning, and tying. Based on these conditions, I could determine the outcome of each round and the overall winner of the game.

Overall, this project expanded my understanding of Python programming concepts and introduced me to more advanced topics such as additional data structures, loops, and conditional statements. It's been a joy getting to see what Python offers and how it compares to my experience with JavaScript!