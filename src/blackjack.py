#Imports
import random

#Constants
MAGIC_SHUFFLE_NUMBER = 7
END_GAME = 21
DEALER_NUMER = 17
ACE_DIFF = 10

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

    # Explicit call to obtain value
    def get_val(self):
        val = self.value
        # Face values equal 10
        if self.value >= 10:
            val = 10
        return val

    # String value
    def __str__(self):
        # Convert 11-13 to Face cards
        if self.value == 11:
            value = "Jack"
        elif self.value == 12:
            value = "Queen"
        elif self.value == 13:
            value = "King"
        elif self.value == 1:
            value = "Ace"
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

    # Return the cards as a list if any
    def get_hand(self):
        return_hand = None
        if len(self.hand) > 0:
            return_hand = self.hand
        return return_hand

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

# Update until human no longer moves
def players_turn(human, game_deck):
    end_value = 0
    ace = 0
    value = None
    cont = True

    # Count player starting hand
    for card in human.get_hand():
        new_value = card.get_val()
        if new_value == 1:
            ace += 1
            new_value = 11
        end_value += new_value

    # Keep hitting until player says end or is over
    while cont:
        value = raw_input("Player, enter Hit or End:")
        cont = value != "End"
        if value == "Hit":
            new_card = game_deck.pop_card()
            new_val = new_card.get_val()
            if new_val == 1:
                ace += 1
                new_val = 11
            end_value += new_val
            print "New card:" + str(new_card)
            human.hit(new_card)
            if end_value > END_GAME:
                # No aces so we broke
                if ace <= 0:
                    cont = False
                # While we have aces to reduce
                while ace > 0:
                    ace -= 1
                    end_value -= ACE_DIFF
                    if end_value < END_GAME:
                        break
    return end_value

# Dealers logic, hit if under 17
def dealers_turn(dealer, game_deck):
    end_value = 0
    ace = 0
    value = None
    cont = True

    # Count player starting hand
    for card in dealer.get_hand():
        new_value = card.get_val()
        if new_value == 1:
            ace += 1
            new_value = 11
        end_value += new_value
        if end_value >= DEALER_NUMER:
            cont = False

    # Keep hitting until player says end or is over
    while cont:
        new_card = game_deck.pop_card()
        new_val = new_card.get_val()
        if new_val == 1:
            ace += 1
            new_val = 11
        end_value += new_val
        dealer.hit(new_card)
        if end_value >= DEALER_NUMER:
            cont = False
        if end_value > END_GAME:
            # No aces so we broke
            if ace <= 0:
                cont = False
            # While we have aces to reduce
            while ace > 0:
                ace -= 1
                end_value -= ACE_DIFF
                if end_value < END_GAME:
                    if end_value < DEALER_NUMER:
                        cont = True
                    break
    return end_value

# Print the end game hands
def print_end_hands(player, dealer):
    print "Player end cards:" + str(player)
    print "Dealer end cards:" + str(dealer)

# Main loop
def main():
    human = Player()
    dealer = Player()
    game_deck = Deck()
    game_deck.shuffle()

    # 1. Start the player and dealer with 2 cards each
    starting_hand(human, dealer, game_deck)

    #2. Loop to allow player to keep hitting
    player_val = players_turn(human, game_deck)

    #3. Logic for dealer only if player didn't bust
    if player_val <= END_GAME:
        dealer_val = dealers_turn(dealer, game_deck)
    # Player bust so set him to -1
    else:
        player_val = -1
        # Since player bust, set dealer to 1 to win
        dealer_val = 1

    # Dealer bust
    if dealer_val > END_GAME:
        dealer_val = -1

    #4. Calulcate winner
    print "Player won!" if player_val > dealer_val else "Dealer won!"
    print_end_hands(human, dealer)

#Call main if not imported
if __name__ == "__main__":
    main()
