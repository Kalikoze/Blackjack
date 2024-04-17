def createDeck():
  suits = ['♠', '♡', '♢', '♣']
  ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
  deck = [(suit, rank) for suit in suits for rank in ranks]
  return deck

deck = createDeck()
print(deck)

def printInstructions():
    print("Welcome to Text-based Blackjack!")
    print("Instructions:")
    print("- Type 'hit' to draw another card")
    print("- Type 'stand' to keep your current hand")

def startGame():
    printInstructions()


startGame()