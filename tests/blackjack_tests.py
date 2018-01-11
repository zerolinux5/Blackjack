import unittest
import sys
import os
parent_dir_name = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
sys.path.append(parent_dir_name + "/src")
import blackjack

class Test_Deck_Class(unittest.TestCase):

    # Create the deck
    def setUp(self):
        self.deck = blackjack.Deck()

    # Test shuffling deck
    def test_shuffle(self):
        first_list = str(self.deck)

        # Test 50 shuffles and verify they are different
        for x in range(50):
            self.deck.shuffle()
            test_list = str(self.deck)
            self.assertNotEqual(first_list, test_list)

    # Test pop deck
    def test_pop_card(self):
        # Test 52 card pop
        for x in range(52):
            self.deck.pop_card()
        self.assertEqual(len(self.deck), 0)

    # Test each card is different
    def test_pop_unique_cards(self):
        list_of_cards = []
        # Test 52 card pop
        for x in range(52):
            new_card = str(self.deck.pop_card())
            self.assertNotIn(new_card, list_of_cards)
            list_of_cards.append(new_card)

class Test_Update_Value_And_Aces(unittest.TestCase):

    # Create the deck
    def setUp(self):
        self.player = blackjack.Player()

    # Test each card is different
    def test_num_aces(self):
        # Add 10 aces
        for x in range(10):
            new_card = blackjack.Card("Spades", 1)
            self.player.hit(new_card)
            num_aces, ignore = blackjack.update_value_and_aces(self.player)
            self.assertEqual(num_aces, x+1)


    # Test each card is different
    def test_total(self):
        count = 0
        # Add 1 - 10
        for x in range(1,11):
            new_card = blackjack.Card("Spades", x)
            self.player.hit(new_card)
            ignore, total = blackjack.update_value_and_aces(self.player)
            # Ace is worth 11 out of context
            if x == 1:
                test = 11
            else:
                test = x
            self.assertEqual(total, count + test)
            count += test

if __name__ == '__main__':
    unittest.main()
