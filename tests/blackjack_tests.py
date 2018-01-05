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

if __name__ == '__main__':
    unittest.main()
