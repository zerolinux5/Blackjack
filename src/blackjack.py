#Imports
import random

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
        random.shuffle(self.deck)

    # Convert Deck to string
    def __str__(self):
        deck_string = ""
        for card in self.deck:
            deck_string += str(card) + " "
        return deck_string

#Card class
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

#Main loop
def main():
    pass

#Call main if not imported
if __name__ == "__main__":
    main()
