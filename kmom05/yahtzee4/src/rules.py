#!/usr/bin/env python3
""" Module for rules in yahtzee """
from abc import ABC, abstractmethod
from src.hand import Hand
#from hand import Hand

class Rule(ABC):
    """ Abstract class for rule """
    @abstractmethod
    def points(self, hand: Hand) -> int:
        """ points function skeleton """

class SameValueRule(Rule):
    """ Class to represent the same value rule """
    def __init__(self, value: int, name: str) -> None:
        self.value = value
        self.name = name

    def points(self, hand: Hand)-> int:
        """ Calculate points for same value rule (sum of equal values)"""
        total = 0
        for value in hand.to_list():
            if value == self.value:
                total += value
        return total

class Ones(SameValueRule):
    """ Ones rule class """
    def __init__(self) -> None:
        super().__init__(1, "Ones")

class Twos(SameValueRule):
    """ Twos rule class """
    def __init__(self) -> None:
        super().__init__(2, "Twos")

class Threes(SameValueRule):
    """ Threes rule class """
    def __init__(self) -> None:
        super().__init__(3, "Threes")

class Fours(SameValueRule):
    """ Fours rule class"""
    def __init__(self) -> None:
        super().__init__(4, "Fours")

class Fives(SameValueRule):
    """ Fives rule class """
    def __init__(self) -> None:
        super().__init__(5, "Fives")

class Sixes(SameValueRule):
    """ Sixes rule class """
    def __init__(self) -> None:
        super().__init__(6, "Sixes")

class ThreeOfAKind(Rule):
    """ Three of a kind rule class """
    def __init__(self) -> None:
        self.name = "Three Of A Kind"

    def points(self, hand) -> int:
        """ Get points for three of a kind """
        occurances = hand.occurances()
        values = occurances.values()
        if 3 in values or 4 in values or 5 in values:
            return hand.sum()
        return 0

class FourOfAKind(Rule):
    """ Four of a kind rule class """
    def __init__(self) -> None:
        self.name = "Four Of A Kind"

    def points(self, hand) -> int:
        """ Get points for four of a kind """
        occurances = hand.occurances()
        if 4 in occurances.values() or 5 in occurances.values():
            return hand.sum()
        return 0

class SmallStraight(Rule):
    """ Small straight rule class """
    def __init__(self) -> None:
        self.name = "Small Straight"

    def points(self, hand) -> int:
        """ Get points for small straight """
        if hand.has_sequence_of_length(4):
            return 30
        return 0

class FullHouse(Rule):
    """ Full house rule class """
    def __init__(self) -> None:
        self.name = "Full House"

    def points(self, hand) -> int:
        """ Get points for full house """
        occurances = hand.occurances()
        o_values = occurances.values()
        if 3 in o_values and 2 in o_values:
            return 25
        return 0

class LargeStraight(Rule):
    """ Large straight rule class """
    def __init__(self) -> None:
        self.name = "Large Straight"

    def points(self, hand) -> int:
        """ Get points for large straigt """
        if hand.has_sequence_of_length(5):
            return 40
        return 0

class Yahtzee(Rule):
    """ Yahtzee rule class """
    def __init__(self) -> None:
        self.name = "Yahtzee"

    def points(self, hand) -> int:
        """ Get points for yahtzee """
        occurances = hand.occurances()
        if 5 in occurances.values():
            return 50
        return 0

class Chance(Rule):
    """ Chance rule class """
    def __init__(self) -> None:
        self.name = "Chance"

    def points(self, hand) -> int:
        """ Get points for chance """
        return hand.sum()
