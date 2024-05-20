import random


def create_deck():
    suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
    ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
    deck = [{'Rank': rank, 'Suit': suit} for suit in suits for rank in ranks]
    random.shuffle(deck)
    return deck

def deal_cards(deck):
    return [deck.pop(), deck.pop()], [deck.pop(), deck.pop()]

def card_visual(card):
    """Chatgpt's card visualization function which returns an card like shape like an actual playing card."""
    rank = card['Rank']
    suit_symbols = {'Hearts': '♥', 'Diamonds': '♦', 'Clubs': '♣', 'Spades': '♠'}
    suit = suit_symbols[card['Suit']]
    return f"""
    ┌─────────┐
    │ {rank.ljust(2)}      │
    │         │
    │    {suit}    │
    │         │
    │      {rank.rjust(2)} │
    └─────────┘
    """

def hand_value(hand, is_player=True):
    """
    Calculates the total value of a hand in Blackjack, automatically choosing the best value for Aces.
    
    Args:
        hand (list): The hand to evaluate, where each card is represented as a dictionary with 'Rank' and 'Suit'.
        is_player (bool): Specifies if the hand belongs to a player, used for differentiating message outputs if needed.

    Returns:
        int: The total value of the hand, with Aces counted as either 1 or 11 to optimize the hand's total value.
    """
    values = {'2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, '10': 10, 'J': 10, 'Q': 10, 'K': 10, 'A': 11}
    result = 0
    aces = 0  # Number of Aces in the hand

    # Calculate initial value of hand and count Aces
    for card in hand:
        if card['Rank'] == 'A':
            aces += 1
        else:
            result += values[card['Rank']]

    # Automatically adjust the value of Aces to get the best possible total value without busting
    for _ in range(aces):
        # Add Ace as 11 if it does not cause the hand to go over 21, otherwise add as 1
        if result + 11 > 21:
            result += 1  # Add as 1 to avoid busting
        else:
            result += 11  # Add as 11 to maximize hand value

    return result




def print_hand(hand):
    """Continuously prints the card_visual function for the given hand"""
    for card in hand:
        print(card_visual(card), end='')

def player_turn(hand, deck):
    """
    The initiation of the player's turn like if the want to hit or stand on a card.

    Args:
    hand (list of dicts): The current hand of the player, where each card is a dictionary containing 'Rank' and 'Suit'.
    deck (list of dicts): The deck from which cards are drawn.

    Returns:
    None: The player's hand is modified in-place, adding new cards as necessary.
    """
    while True:
        print("Your current hand:")
        print_hand(hand)
        print(f"Total value: {hand_value(hand)}\n")

        if hand_value(hand) >= 21:
            break

        while True: # Loop to handle input validation
            action = input("Do you want to hit or stand? (hit/stand): ").lower()
            if action in ['hit', 'stand']:
               break
            else:
                print("Invalid input...Please enter a hit or stand.")

        if action == 'hit':
            hand.append(deck.pop())
        elif action == 'stand':
            break

def dealer_turn(hand, deck):
    """Similar to the player's turn but with no inputs needed and dealers are not allowed to hit with a hand of 17 or more."""
    while hand_value(hand) < 17:
        hand.append(deck.pop())

def check_winner(player_hand, dealer_hand, bet, player_money, dealer_money):
    """
    Determines the outcome of a Blackjack game round and updates financial stakes.

    This function compares the values of the player's and dealer's hands and adjusts their monetary stakes based on the game rules. It handles different outcomes like player busts, dealer busts, natural blackjack, and ties.

    Args:
    player_hand (list of dicts): The player's current hand.
    dealer_hand (list of dicts): The dealer's current hand.
    bet (int): The amount of money bet at the start of the round.
    player_money (int): Current total money of the player.
    dealer_money (int): Current total money of the dealer.

    Returns:
    tuple: A message describing the result of the round, updated dealer's money, and updated player's money.
    """
    player_score = hand_value(player_hand)
    dealer_score = hand_value(dealer_hand)

    # Display the final hands and scores
    print("\nFinal hands:")
    print("Dealer's hand:")
    print_hand(dealer_hand)
    print(f"Dealer's total: {dealer_score}")

    print("\nPlayer's hand:")
    print_hand(player_hand)
    print(f"Player's total: {player_score}")

    # Determine the winner and adjust finances accordingly
    if player_score > 21:
        dealer_money += bet
        return f"\nDealer wins, Player busted! Dealer's final score: {dealer_score}", dealer_money, player_money - bet
    elif player_score == 21 and len(player_hand) == 2 and any(card['Rank'] in ['10', 'J', 'Q', 'K'] for card in player_hand):
        # Blackjack win, payout is 3 to 2
        winnings = int(1.5 * bet)
        player_money += winnings
        dealer_money -= winnings
        return f"\nBlackjack! Player wins! Dealer's final score: {dealer_score}", dealer_money, player_money
    elif dealer_score > 21:
        player_money += bet * 1  # Player wins the bet and gets back their original bet
        dealer_money -= bet
        return f"\nPlayer wins! Dealer Busted! Dealer's final score: {dealer_score}", dealer_money, player_money
    elif player_score > dealer_score:
        player_money += bet * 1  # Player wins the bet and gets back their original bet
        dealer_money -= bet
        return f"\nPlayer wins! Dealer's final score: {dealer_score}", dealer_money, player_money
    elif player_score < dealer_score:
        dealer_money += bet
        return f"\nDealer wins! Dealer's final score: {dealer_score}", dealer_money, player_money - bet
    else:
        # Correct handling of a tie, player gets their bet back
        return f"\nIt's a tie! Dealer's final score: {dealer_score}", dealer_money, player_money



def blackjack_game():
    """
    Starts and conducts the game of Blackjack between a player and a dealer.

    This function manages the game loop where the player and dealer bet, draw cards, and determine the round outcomes. 
    The game continues until the player opts out, runs out of money, or the dealer runs out of money. 
    Each round involves the player placing a bet, receiving cards, and making decisions on their play based on the game's progress.
    The game can be restarted completely if the player opts to play again after a game over.

    
    Args:
    None: This function does not take any arguments but relies on the global state of the player's and dealer's money.
    
    Returns:
    None: This function manages the game loop and outputs directly to the console, but does not return any values.
    
    The player starts with $100 and the dealer starts with $1000. The player's turn allows them to hit or stand based on the value of their hand,
    and the dealer automatically plays according to Blackjack which are (established above) rules. Results are printed each round, and the game ends based on the player's choice or financial status.
    """

    while True:  # This outer loop restarts the game completely
        initial_money = 100
        player_money = initial_money
        dealer_money = 1000

        while True:
            if player_money <= 0:
                print("You've run out of money!")
                restart = input("Would you like to play again? (y/n): ").lower()
                if restart == 'y':
                    print("Restarting the game...")
                    break  # Breaks the inner loop to restart the game
                else:
                    print("Thank you for playing!")
                    return  # Exits the function and thus ends the game

            print(f"Player's money: ${player_money}, Dealer's money: ${dealer_money}")

            # Collect bet from player
            while True:
                try:
                    bet = int(input("Place your bet: "))
                    if 0 < bet <= player_money:
                        break
                    else:
                        print(f"Invalid bet. You can bet between $1 and ${player_money}.")
                except ValueError:
                    print("Please enter a valid number.")

            # Game setup or reset for a new round
            deck = create_deck()
            player_hand, dealer_hand = deal_cards(deck)

            # Display one of the dealer's cards
            print("Dealer's visible card:")
            print(card_visual(dealer_hand[0]))

            # Game round loop
            player_turn(player_hand, deck)
            if hand_value(player_hand) <= 21:
                dealer_turn(dealer_hand, deck)

            result, dealer_money, player_money = check_winner(player_hand, dealer_hand, bet, player_money, dealer_money)
            print(result)
            
            if player_money > 0:
                response = input("Would you like to play another round? (y/n): ").lower()
                if response != 'y':
                    print(f"Thanks for playing! You ended the game with ${player_money}.")
                    break  # Break the inner loop if not continuing the current game session

blackjack_game()