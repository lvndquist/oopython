#!/usr/bin/env python3
""" Module for testing the class Hand """

import unittest
import random
from src.hand import Hand

class TestHand(unittest.TestCase):
    """ Submodule for unittests, derives from unittest.TestCase """
    def setUp(self) -> None:
        """ Setup that runs before every testcase """
        random.seed("die")

    def test_hand_no_arg(self) -> None:
        """ Test hand creation without any arguments """
        # [5, 5, 4, 3, 3]
        hand = Hand()
        self.check_hand_length(hand)
        self.check_hand_die_values(hand, [5, 5, 4, 3, 3])

    def test_hand_with_args(self) -> None:
        """ Test hand creation using lists with different lengths
        """

        #[1, 5, 5, 4, 3]
        hand1 = Hand([1])
        self.check_hand_length(hand1)
        self.check_hand_die_values(hand1, [1, 5, 5, 4, 3])

        #[1, 2, 3, 4, 2]
        hand2 = Hand([1, 2])
        self.check_hand_length(hand2)
        self.check_hand_die_values(hand2, [1, 2, 3, 4, 2])

        #[1, 2, 4, 1, 4]
        hand3 = Hand([1, 2, 4])
        self.check_hand_length(hand3)
        self.check_hand_die_values(hand3, [1, 2, 4, 1, 4])

        #[1, 2, 5, 6, 4]
        hand4 = Hand([1, 2, 5, 6])
        self.check_hand_length(hand4)
        self.check_hand_die_values(hand4, [1, 2, 5, 6, 4])

        #[1, 2, 5, 6, 3]
        hand5 = Hand([1, 2, 5, 6, 3])
        self.check_hand_length(hand5)
        self.check_hand_die_values(hand5, [1, 2, 5, 6, 3])

        #[1, 2, 3, 5, 6]
        hand6 = Hand([1, 2, 3, 5, 6, 1])
        self.check_hand_length(hand6)
        self.check_hand_die_values(hand6, [1, 2, 3, 5, 6])

    def test_hand_roll_with_args(self) -> None:
        """ Test re rolling die at specific index in hand """
        hand = Hand([1, 2, 3, 4, 5])
        # re roll all but first die -> 1, 5, 5, 4, 3
        hand.roll([1, 2, 3, 4])
        self.check_hand_die_values(hand, [1, 5, 5, 4, 3])

    def test_hand_roll_no_args(self) -> None:
        """ Test rolling with no arguments """
        hand = Hand() # 5, 5, 4, 3, 3
        hand.roll() # 4, 2, 1, 4, 4
        self.check_hand_die_values(hand, [4, 2, 1, 4, 4])

    def check_hand_length(self, hand: Hand) -> None:
        """ Assert the length of a hand to see if its 5 """
        self.assertEqual(len(hand.dice), 5)

    def check_hand_die_values(self, hand: Hand, control_values: list[int]) -> None:
        """ Assert if the dice values are integer, between 1 and 6 and correct 
            based on given control values
        """
        for die, control_value in zip(hand.dice, control_values):

            # Value of the die should be integer
            self.assertIsInstance(die.value, int)

            # Value of the die should be between 1 and 6
            self.assertTrue(1 <= die.value <= 6)

            # Value of the die should be same as the control value
            self.assertEqual(die.value, control_value)
