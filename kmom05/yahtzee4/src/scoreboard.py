#!/usr/bin/env python3
""" Module for scoreboard in yahtzee """

from src.hand import Hand
from src.rules import Ones, Twos, Threes, Fours, Fives, Sixes
from src.rules import ThreeOfAKind, FourOfAKind, SmallStraight
from src.rules import LargeStraight, FullHouse, Yahtzee, Chance

class Scoreboard:
    """ Class representing a scoreboard """

    rules = {
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

    def __init__(self) -> None:
        temp_dict = {}
        for rule in self.rules:
            temp_dict[rule] = -1
        self._points = temp_dict

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

    def get_hand_points(self, rule_name: str, hand: Hand) -> int:
        """ Calculate points in a hand using a rule """
        return self.rules[rule_name]().points(hand)

    def add_points(self, rule_name: str, hand: Hand) -> None:
        """ Add points based on contents of a hand and some rule """
        if not rule_name:
            raise KeyError(f"{rule_name} is not a valid rule!")

        #if rule_name not in self.points.keys():
        #    self.points[rule_name] = -1

        if self.points[rule_name] != -1:
            raise ValueError(f"{rule_name} has already been used!")

        self.points[rule_name] = self.get_hand_points(rule_name, hand)

    def get_points(self, rule_name: str) -> int:
        """ Get points based on name of the rule used to obtain the points """
        if rule_name in self.points.keys():
            return self.points[rule_name]
        return -1

    def finished(self) -> bool:
        """ Check if all rules have been used """
        if not self.points.values():
            return False
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
