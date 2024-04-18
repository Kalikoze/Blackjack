def createDeck():
  ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
  suits = ['♠', '♡', '♢', '♣']
  deck = [(rank, suit) for rank in ranks for suit in suits]
  return deck

deck = createDeck()
player_hand = []
dealer_hand = []

def getRandomCard(deck):
    import random
    random_index = random.randint(0, len(deck) - 1)
    return deck.pop(random_index)

def calculate_hand(hand):
    total = 0
    for card in hand:
        rank = card[1]
        if rank in ['J', 'Q', 'K']:
            total += 10
        elif rank == 'A':
            total += 11
        else:
            total += int(rank)
    return total

def printInstructions():
    print("Welcome to Text-based Blackjack! \n")
    print("Instructions:")
    print("- Type 'hit' to draw another card")
    print("- Type 'stand' to keep your current hand \n")
    print(f"Player's Hand: {''.join(player_hand)} Total: {calculate_hand(player_hand)} \n")
    print(f"Dealer's Hand: [?]{dealer_hand[-1]} \n")


def deal_initial_hands():
    for i in range(2):
        rank, suit = getRandomCard(deck)
        player_hand.append(str(f"[{rank}{suit}]"))
        rank, suit = getRandomCard(deck)
        dealer_hand.append(str(f"[{rank}{suit}]"))

def get_player_input():
    player_input = input("Do you want to hit or stand? (hit/stand): ")
    if player_input == 'hit':
        rank, suit = getRandomCard(deck)
        player_hand.append(str(f"[{rank}{suit}]"))
        print(f"Player's Hand: {''.join(player_hand)} Total: {calculate_hand(player_hand)} \n")
        get_player_input()
    elif player_input == 'stand':
        print("Player stands")
    else:
        print("Invalid input. Please type 'hit' or 'stand'.")
        get_player_input()

def startGame():
    deal_initial_hands()
    printInstructions()
    get_player_input()


startGame()