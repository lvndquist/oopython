#!/usr/bin/env python3
""" Module for testing the class scoreboard """

import unittest
from src.unorderedlist import UnorderedList
from src.errors import MissingValue, MissingIndex

class TestUnorderedList(unittest.TestCase):
    """ Submodule for unittests, derives from unittest.TestCase """

    def setUp(self) -> None:
        """ Setup that runs before every testcase """
        self.ul = UnorderedList()
        self.ul.append(1)
        self.ul.append(2)
        self.ul.append(3)

    def test_get_exception(self):
        """  Test using get function with invalid indices """
        with self.assertRaises(MissingIndex) as _:
            self.ul.get(3)
        with self.assertRaises(MissingIndex) as _:
            self.ul.get(-1)

    def test_get_correct(self):
        """Test using get function with valid indices"""
        self.assertEqual(self.ul.get(0), 1)
        self.assertEqual(self.ul.get(1), 2)
        self.assertEqual(self.ul.get(2), 3)

    def test_remove_exception(self):
        """Test removing a value that doesnt exist """
        with self.assertRaises(MissingValue) as _:
            self.ul.remove(4)

    def test_remove_correct(self):
        """Test removing a value that exists """
        removed = self.ul.remove(1)
        self.assertEqual(removed, 1)

        removed = self.ul.remove(3)
        self.assertEqual(removed, 3)

        removed = self.ul.remove(2)
        self.assertEqual(removed, 2)
