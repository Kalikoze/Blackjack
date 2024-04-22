def createDeck():
  ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
  suits = ['♠', '♡', '♢', '♣']
  deck = [(rank, suit) for rank in ranks for suit in suits]
  return deck

deck = createDeck()
player_hand = []
dealer_hand = []
wins, losses = 0, 0

def getRandomCard(deck):
    import random
    random_index = random.randint(0, len(deck) - 1)
    return deck.pop(random_index)

def calculate_hand(hand):
    total = 0
    for (rank, suit) in hand:
        if rank in ['J', 'Q', 'K']:
            total += 10
        elif rank == 'A':
            total += 11
        else:
            total += int(rank)
    return total

def format_card(hand):
    formatted_hand = []
    for (rank, suit) in hand:
        formatted_hand.append(f"[{rank}{suit}]")
    return ''.join(formatted_hand)

def printInstructions():
    print("Welcome to Text-based Blackjack! \n")
    print("Instructions:")
    print("- Type 'hit' to draw another card")
    print("- Type 'stand' to keep your current hand \n")
    print(f"Player's Hand: {format_card(player_hand)} Total: {calculate_hand(player_hand)} \n")
    print(f"Dealer's Hand: [?]{format_card([dealer_hand[-1]])} \n")

def display_stats():
    print(f"Wins: {wins} \nLosses: {losses} \nWin Percentage: {wins / (wins + losses) * 100}% \n")

def deal_initial_hands():    
    for i in range(2):
        rank, suit = getRandomCard(deck)
        player_hand.append((rank, suit))
        rank, suit = getRandomCard(deck)
        dealer_hand.append((rank, suit))

def determine_bust():
    global losses
    if calculate_hand(player_hand) > 21:
        print(f"Player's Hand: [] Total: {calculate_hand(player_hand)} \n")
        print("Bust! You lose.")
        losses += 1
        display_stats()
        exit()

def dealer_plays():
    global wins, losses
    dealer_total = calculate_hand(dealer_hand)
    while dealer_total < 17:
        print("Dealer hits. \n")
        rank, suit = getRandomCard(deck)
        dealer_hand.append((rank, suit))
        dealer_total = calculate_hand(dealer_hand)
        print(f"Dealer draws: [{rank}{suit}] \n")
    if dealer_total > 21:
        print(f"Dealer's Hand: {format_card(dealer_hand)} Total: {dealer_total} \n")
        print(f"Dealer busts! You win! Your hand: {calculate_hand(player_hand)} vs Dealer's hand: {calculate_hand(dealer_hand)} \n")
        wins += 1
        display_stats()
        exit()
    else:
        print(f"Dealer's Hand: {format_card(dealer_hand)} Total: {dealer_total} \n")
        if calculate_hand(player_hand) > dealer_total:
            print(f"Player wins!  You win! Your hand: {calculate_hand(player_hand)} vs Dealer's hand: {calculate_hand(dealer_hand)} \n")
            wins += 1
            display_stats()
        else:
            print(f"Dealer wins. Your hand: {calculate_hand(player_hand)} vs Dealer's hand: {calculate_hand(dealer_hand)} \n")
            losses += 1
            display_stats()
        exit()

def get_player_input():
    player_input = input("Do you want to hit or stand? (hit/stand): ")
    if player_input == 'hit':
        rank, suit = getRandomCard(deck)
        player_hand.append((rank, suit))
        determine_bust()
        print(f"\n Player's Hand: {format_card(player_hand)} Total: {calculate_hand(player_hand)} \n")
        get_player_input()
    elif player_input == 'stand':
        print(f"\n Player's Hand: {format_card(player_hand)} Total: {calculate_hand(player_hand)} \n")
        print("Dealer's Turn: \n")
        dealer_plays()
    else:
        print("Invalid input. Please type 'hit' or 'stand'.")
        get_player_input()

def startGame():
    deal_initial_hands()
    printInstructions()
    get_player_input()


startGame()