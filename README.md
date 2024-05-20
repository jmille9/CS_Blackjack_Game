# Blackjack Game

This is a simple console-based Blackjack game implemented in Python. The game allows a player to play against the dealer, with basic Blackjack rules and betting system. 

## Features

- Creation and shuffling of a standard 52-card deck.
- Dealing of initial hands to the player and dealer.
- Visualization of cards in a card-like shape.
- Calculation of hand values with proper handling of Aces.
- Player turn with options to hit or stand.
- Dealer turn with automatic play according to standard Blackjack rules.
- Determination of the winner and adjustment of financial stakes.
- Game loop allowing multiple rounds and handling player’s financial status.

## How to Play

1. **Starting the Game**: The game starts with the player having $100 and the dealer having $1000.
2. **Placing Bets**: The player places a bet at the beginning of each round.
3. **Dealing Cards**: The player and dealer are each dealt two cards.
4. **Player’s Turn**: The player can choose to hit (draw a card) or stand (end their turn). The player's turn continues until they stand or their hand value reaches or exceeds 21.
5. **Dealer’s Turn**: The dealer draws cards until their hand value is at least 17.
6. **Determining the Winner**: The winner is determined based on the hand values of the player and dealer.
7. **Continuing the Game**: The player can choose to play another round or end the game.

## Game Rules

- **Hand Value Calculation**: 
  - Number cards (2-10) are worth their face value.
  - Face cards (J, Q, K) are worth 10 points.
  - Aces can be worth 1 or 11 points, whichever is more advantageous without busting the hand.
  
- **Blackjack**: A hand with an Ace and a 10-point card (10, J, Q, K) on the initial deal is a Blackjack and wins with a payout of 1.5 times the bet, unless the dealer also has a Blackjack.

- **Winning and Losing**: 
  - If the player busts (hand value exceeds 21), they lose the bet.
  - If the dealer busts, the player wins the bet.
  - If neither busts, the hand with the higher value wins.
  - In case of a tie, the player gets their bet back.

## Code Overview

### `create_deck()`
Creates and shuffles a standard 52-card deck.

### `deal_cards(deck)`
Deals two cards each to the player and dealer from the deck.

### `card_visual(card)`
Returns a string representing a card in a card-like shape for visualization.

### `hand_value(hand, is_player=True)`
Calculates the total value of a hand, optimizing Ace values.

### `print_hand(hand)`
Prints the visual representation of a hand.

### `player_turn(hand, deck)`
Manages the player's turn, allowing them to hit or stand.

### `dealer_turn(hand, deck)`
Manages the dealer's turn, drawing cards until the hand value is at least 17.

### `check_winner(player_hand, dealer_hand, bet, player_money, dealer_money)`
Determines the winner of the round and adjusts the financial stakes.

### `blackjack_game()`
Main game loop that manages the overall flow of the game, including betting, dealing, and determining outcomes.

## Running the Game

To run the game, execute the `blackjack_game()` function. The game will prompt for user inputs and display the game status in the console.

```python
blackjack_game()

An example game is:

Player's money: $100, Dealer's money: $1000
Place your bet: 20
Dealer's visible card:
    ┌─────────┐
    │ 5       │
    │         │
    │    ♥    │
    │         │
    │       5 │
    └─────────┘
Your current hand:
    ┌─────────┐
    │ 8       │
    │         │
    │    ♠    │
    │         │
    │       8 │
    └─────────┘
    ┌─────────┐
    │ A       │
    │         │
    │    ♦    │
    │         │
    │       A │
    └─────────┘
Total value: 19

Do you want to hit or stand? (hit/stand): stand

Final hands:
Dealer's hand:
    ┌─────────┐
    │ 5       │
    │         │
    │    ♥    │
    │         │
    │       5 │
    └─────────┘
    ┌─────────┐
    │ 9       │
    │         │
    │    ♠    │
    │         │
    │       9 │
    └─────────┘
Dealer's total: 14

Player's hand:
    ┌─────────┐
    │ 8       │
    │         │
    │    ♠    │
    │         │
    │       8 │
    └─────────┘
    ┌─────────┐
    │ A       │
    │         │
    │    ♦    │
    │         │
    │       A │
    └─────────┘
Player's total: 19

Player wins! Dealer's final score: 14

