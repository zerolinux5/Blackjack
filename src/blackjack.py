#Imports
import random

#Constants
MAGIC_SHUFFLE_NUMBER = 7

#Game deck, used to shuffle and keep track of cards
class Deck(object):
    # 4 Suits
    suits = ["Hearts", "Diamonds", "Clubs", "Spades"]
    # 13 different values, last 3 are face cards worth 10
    values = range(1,14)

    # Initialize the deck
    def __init__(self):
        self.deck = []
        # For each suite
        for suit in Deck.suits:
            #For each card value
            for value in Deck.values:
                #Add card to deck
                new_card = Card(suit, value)
                self.deck.append(new_card)

    # Shuffle the deck
    def shuffle(self):
        # Magic number to fully shuffled deck
        for x in range(MAGIC_SHUFFLE_NUMBER):
            random.shuffle(self.deck)

    # Pop top card
    def pop_card(self):
        top_card = self.deck.pop()
        return top_card

    # Define len
    def __len__(self):
        return len(self.deck)

    # Convert Deck to string
    def __str__(self):
        deck_string = ""
        for card in self.deck:
            deck_string += str(card) + " "
        return deck_string

#Card class, keep track of suit and value.
class Card(object):

    # Initialize card with suit and value
    def __init__(self, suit, value):
        self.suit = suit
        self.value = value

    # Explicit call to obtain Suit
    def get_suit(self):
        return self.suit

    # String value
    def __str__(self):
        # Convert 11-13 to Face cards
        if self.value == 11:
            value = "Jack"
        elif self.value == 12:
            value = "Queen"
        elif self.value == 13:
            value = "King"
        else:
            value = str(self.value)

        #Return suit and value
        return self.suit + " " + value

#Player class, keep track of cards in hand.
class Player(object):

    # Every player starts with no hand
    def __init__(self):
        self.hand = []

    # Add card to hand
    def hit(self, card):
        self.hand.append(card)

    # Return every card in hand
    def __str__(self):
        hand_string = ""
        for card in self.hand:
            hand_string += str(card) + " "
        return hand_string

    # Length is based off of hand size
    def __len__(self):
        return len(self.hand)

# Start the game
def starting_hand(human, dealer, game_deck):
    for x in range(2):
        new_card = game_deck.pop_card()
        human.hit(new_card)
        new_card = game_deck.pop_card()
        dealer.hit(new_card)
        #Cheat by calling hand when only 1 card is present
        if x == 0:
            dealer_card = str(dealer)

    print "Dealer cards: X X " + dealer_card
    print "Player cards:" + str(human)

# Main loop
def main():
    human = Player()
    dealer = Player()
    game_deck = Deck()
    game_deck.shuffle()

    # 1. Start the player and dealer with 2 cards each
    starting_hand(human, dealer, game_deck)

#Call main if not imported
if __name__ == "__main__":
    main()
