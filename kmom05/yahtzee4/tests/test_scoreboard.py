#!/usr/bin/env python3
""" Module for testing the class scoreboard """

import unittest
import random
from src.scoreboard import Scoreboard
from src.hand import Hand

class TestScoreboard(unittest.TestCase):
    """ Submodule for unittests, derives from unittest.TestCase """
    def setUp(self) -> None:
        """ Setup that runs before every testcase """
        random.seed("die")

    def test_add_points_not_taken(self):
        """ Test adding points """
        hand = Hand() # 5, 5, 4, 3, 3
        scoreboard = Scoreboard()
        scoreboard.add_points("Fives", hand)
        points = scoreboard.get_points("Fives")
        self.assertEqual(points, 10)

    def test_add_points_taken(self):
        """ Test adding points with a rule that has already been used """
        hand = Hand() # 5, 5, 4, 3, 3
        scoreboard = Scoreboard()
        scoreboard.add_points("Threes", hand)
        hand2 = Hand([3, 3, 3, 2, 1])
        with self.assertRaises(ValueError) as _:
            scoreboard.add_points("Threes", hand2)
