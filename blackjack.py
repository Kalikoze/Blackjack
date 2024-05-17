import random

# Constants
RANKS = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
SUITS = ['♠', '♡', '♢', '♣']

def create_deck():
    return [(rank, suit) for rank in RANKS for suit in SUITS]

def get_random_card(deck):
    random_index = random.randint(0, len(deck) - 1)
    return deck.pop(random_index)

def calculate_hand(hand):
    total, aces = calculate_initial_total_and_aces(hand)
    total = adjust_for_aces(total, aces)
    return total

def calculate_initial_total_and_aces(hand):
    total = 0
    aces = 0
    for (rank, suit) in hand:
        if rank in ['J', 'Q', 'K']:
            total += 10
        elif rank == 'A':
            total += 11
            aces += 1
        else:
            total += int(rank)
    return total, aces

def adjust_for_aces(total, aces):
    while total > 21 and aces:
        total -= 10
        aces -= 1
    return total

def format_hand(hand):
    return ''.join([f"[{rank}{suit}]" for rank, suit in hand])

def print_instructions(player_hand, dealer_hand):
    print("Welcome to Text-based Blackjack! \n")
    print("Instructions:")
    print("- Type 'hit' to draw another card")
    print("- Type 'stand' to keep your current hand \n")
    print(f"Player's Hand: {format_hand(player_hand)} Total: {calculate_hand(player_hand)} \n")
    print(f"Dealer's Hand: [?]{format_hand([dealer_hand[-1]])} \n")

def display_stats(wins, losses):
    total_games = wins + losses
    win_percentage = (wins / total_games * 100) if total_games > 0 else 0
    print(f"Wins: {wins} \nLosses: {losses} \nWin Percentage: {win_percentage:.2f}% \n")

def deal_initial_hands(deck):
    player_hand = [get_random_card(deck) for _ in range(2)]
    dealer_hand = [get_random_card(deck) for _ in range(2)]
    return player_hand, dealer_hand

def determine_bust(player_hand, losses):
    if calculate_hand(player_hand) > 21:
        print(f"Player's Hand: {format_hand(player_hand)} Total: {calculate_hand(player_hand)} \n")
        print("Bust! You lose.")
        losses += 1
        return True, losses
    return False, losses

def dealer_hits(deck, dealer_hand):
    dealer_total = calculate_hand(dealer_hand)
    while dealer_total < 17:
        print("Dealer hits. \n")
        dealer_hand.append(get_random_card(deck))
        dealer_total = calculate_hand(dealer_hand)
        print(f"Dealer draws: {format_hand([dealer_hand[-1]])} \n")
    return dealer_total

def dealer_busts(dealer_total, player_hand, dealer_hand, wins):
    print(f"Dealer's Hand: {format_hand(dealer_hand)} Total: {dealer_total} \n")
    print(f"Dealer busts! You win! Your hand: {calculate_hand(player_hand)} vs Dealer's hand: {dealer_total} \n")
    wins += 1
    return wins

def compare_hands(dealer_total, player_hand, dealer_hand, wins, losses):
    print(f"Dealer's Hand: {format_hand(dealer_hand)} Total: {dealer_total} \n")
    player_total = calculate_hand(player_hand)
    if player_total > dealer_total:
        print(f"Player wins! Your hand: {player_total} vs Dealer's hand: {dealer_total} \n")
        wins += 1
    else:
        print(f"Dealer wins. Your hand: {player_total} vs Dealer's hand: {dealer_total} \n")
        losses += 1
    return wins, losses

def dealer_plays(deck, player_hand, dealer_hand, wins, losses):
    dealer_total = dealer_hits(deck, dealer_hand)
    if dealer_total > 21:
        wins = dealer_busts(dealer_total, player_hand, dealer_hand, wins)
    else:
        wins, losses = compare_hands(dealer_total, player_hand, dealer_hand, wins, losses)
    return wins, losses

def main():
    wins = 0
    losses = 0
    while True:
        deck, player_hand, dealer_hand = start_new_game()
        wins, losses = play_game(deck, player_hand, dealer_hand, wins, losses)
        display_stats(wins, losses)
        if not play_again():
            break

def start_new_game():
    deck = create_deck()
    player_hand, dealer_hand = deal_initial_hands(deck)
    print_instructions(player_hand, dealer_hand)
    return deck, player_hand, dealer_hand

def play_game(deck, player_hand, dealer_hand, wins, losses):
    while True:
        action = get_player_action()
        if action == 'hit':
            player_hand.append(get_random_card(deck))
            print(f"Player draws: {format_hand([player_hand[-1]])} \n")
            print(f"Player's Hand: {format_hand(player_hand)} Total: {calculate_hand(player_hand)} \n")
            busted, losses = determine_bust(player_hand, losses)
            if busted:
                break
        elif action == 'stand':
            wins, losses = dealer_plays(deck, player_hand, dealer_hand, wins, losses)
            break
    return wins, losses

def get_player_action():
    while True:
        action = input("What would you like to do? (hit/stand) \n").lower()
        if action in ['hit', 'stand']:
            return action
        print("Invalid action. Please type 'hit' or 'stand'. \n")

def play_again():
    while True:
        play_again = input("Do you want to play again? (yes/no) \n").lower()
        if play_again in ['yes', 'no']:
            return play_again == 'yes'
        print("Invalid input. Please type 'yes' or 'no'. \n")

if __name__ == "__main__":
    main()
