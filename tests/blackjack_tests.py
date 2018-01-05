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

if __name__ == '__main__':
    unittest.main()
