import random

# Card values and suits
suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
values = {'2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, '10': 10, 'J': 10, 'Q': 10, 'K': 10, 'A': 11}

# Function to create a deck
def create_deck():
    deck = []
    for suit in suits:
        for rank in ranks:
            deck.append((rank, suit))
    random.shuffle(deck)
    return deck

# Function to calculate hand value
def calculate_hand_value(hand):
    value = 0
    ace_count = 0
    for card in hand:
        rank = card[0]
        value += values[rank]
        if rank == 'A':
            ace_count += 1

    while value > 21 and ace_count:
        value -= 10  # Treat Ace as 1 instead of 11
        ace_count -= 1

    return value

# Function to display the hands
def display_hands(player_hand, dealer_hand, reveal_dealer=False):
    print("\nPlayer's hand:", ', '.join(f"{card[0]} of {card[1]}" for card in player_hand))
    print("Player's hand value:", calculate_hand_value(player_hand))
    if reveal_dealer:
        print("Dealer's hand:", ', '.join(f"{card[0]} of {card[1]}" for card in dealer_hand))
        print("Dealer's hand value:", calculate_hand_value(dealer_hand))
    else:
        print("Dealer's hand: [Hidden, " + f"{dealer_hand[1][0]} of {dealer_hand[1][1]}" + "]")

# Function for player's turn
def player_turn(deck, player_hand):
    while True:
        choice = input("Do you want to 'hit' or 'stand'? ").lower()
        if choice == 'hit':
            player_hand.append(deck.pop())
            display_hands(player_hand, dealer_hand)
            if calculate_hand_value(player_hand) > 21:
                print("Player busts! Dealer wins.")
                return False
        elif choice == 'stand':
            return True
        else:
            print("Invalid input. Please choose 'hit' or 'stand'.")

# Function for dealer's turn
def dealer_turn(deck, dealer_hand):
    while calculate_hand_value(dealer_hand) < 17:
        print("\nDealer hits!")
        dealer_hand.append(deck.pop())
        display_hands(player_hand, dealer_hand, reveal_dealer=True)
        if calculate_hand_value(dealer_hand) > 21:
            print("Dealer busts! Player wins.")
            return False
    return True

# Main game function
def play_blackjack():
    deck = create_deck()
    player_hand = [deck.pop(), deck.pop()]
    dealer_hand = [deck.pop(), deck.pop()]

    print("Welcome to Blackjack!\n")
    display_hands(player_hand, dealer_hand)

    if not player_turn(deck, player_hand):
        return

    if not dealer_turn(deck, dealer_hand):
        return

    player_value = calculate_hand_value(player_hand)
    dealer_value = calculate_hand_value(dealer_hand)

    if player_value > dealer_value:
        print("\nPlayer wins!")
    elif player_value < dealer_value:
        print("\nDealer wins!")
    else:
        print("\nIt's a tie!")

if __name__ == "__main__":
    play_blackjack()
