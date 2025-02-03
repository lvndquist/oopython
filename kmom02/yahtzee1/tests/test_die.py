#!/usr/bin/env python3
""" Module for testing the class Die """

import unittest
import random
from src.die import Die

class TestDie(unittest.TestCase):
    """ Submodule for unittests, derives from unittest.TestCase """
    def setUp(self):
        """ Setup that runs before every testcase """
        random.seed("die")

    def test_die_no_arg(self):
        """ Test creating a die without argument """
        die = Die() # 5 with seed
        die_val = die.get_value()
        self.assertEqual(die_val, 5)

    def test_die_arg(self):
        """ Test creating a die with argument """
        die_set_val = 3
        die = Die(die_set_val)
        die_val = die.get_value()
        self.assertEqual(die_val, die_set_val)

    def test_die_large_arg(self):
        """ Test creating a die with too big argument """
        die = Die(100)
        die_val = die.get_value()
        self.assertEqual(die_val, 6)

    def test_die_small_arg(self):
        """ Test creating a die with too small argument """
        die = Die(0)
        die_val = die.get_value()
        self.assertEqual(die_val, 1)

    def test_roll(self):
        """ Test random roll """
        die = Die(2)
        start_val = die.get_value()
        die.roll() # gives 5 with given seed
        end_val = die.get_value()
        self.assertNotEqual(start_val, end_val)

    def test_get_name(self):
        """ Test correct naming """
        die = Die(4)
        name = die.get_name()
        self.assertEqual(name, "four")
