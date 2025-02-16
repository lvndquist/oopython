#!/usr/bin/env python3
""" Module for scoreboard in yahtzee """

from src.hand import Hand
from src.rules import Ones, Twos, Threes, Fours, Fives, Sixes
from src.rules import ThreeOfAKind, FourOfAKind, SmallStraight
from src.rules import LargeStraight, FullHouse, Yahtzee, Chance

class Scoreboard:
    """ Class representing a scoreboard """
    def __init__(self) -> None:
        self._points = {}

    def get_total_points(self) -> int:
        """ Get the total points """
        total = 0
        for rule in self.points.values():
            if rule != -1:
                total += rule
        return total

    @property
    def points(self) -> dict[str, int]:
        """ Points attribute getter """
        return self._points

    def add_points(self, rule_name: str, hand: Hand) -> None:
        """ Add points based on contents of a hand and some rule """
        points = 0
        if self.points[rule_name] != -1:
            raise ValueError(f"{rule_name} has already been used!")

        callables = {
            "Ones": Ones,
            "Twos": Twos,
            "Threes": Threes,
            "Fours": Fours,
            "Fives": Fives,
            "Sixes": Sixes,
            "Three Of A Kind": ThreeOfAKind,
            "Four Of A Kind": FourOfAKind,
            "Small Straight": SmallStraight,
            "Large Straight": LargeStraight,
            "Full House": FullHouse,
            "Yahtzee": Yahtzee,
            "Chance": Chance
        }

        points = callables[rule_name]().points(hand)
        self.points[rule_name] = points

    def get_points(self, rule_name: str) -> int:
        """ Get points based on name of the rule used to obtain the points """
        if rule_name in self.points.keys():
            return self.points[rule_name]
        return -1

    def finished(self) -> bool:
        """ Check if all rules have been used """
        for score in self.points.values():
            if score == -1:
                return False
        return True

    @classmethod
    def from_dict(cls, points: dict[str, int]) -> object:
        """ Create scoreboard object from a dict"""
        scoreboard = cls()
        scoreboard._points = points
        return scoreboard
