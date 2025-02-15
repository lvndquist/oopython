#!/usr/bin/env python3
""" Module for a die in yahtzee """

import random

class Die():
    """ Die class """
    MIN_ROLL_VALUE = 1
    MAX_ROLL_VALUE = 6
    def __init__(self, value = None) -> None:
        """ Die constructor """
        self._value = self.check_value(value)

    def get_name(self) -> str:
        """ Gets string representation of die value """
        die_str = "one"
        if self._value == 2:
            die_str = "two"
        elif self._value == 3:
            die_str = "three"
        elif self._value == 4:
            die_str = "four"
        elif self._value == 5:
            die_str = "five"
        elif self._value == 6:
            die_str = "six"
        return die_str

    @property
    def value(self) -> int:
        """ Gets the value of a die """
        return self._value

    def check_value(self, value) -> int:
        """ Sets the value of a die based on input value """
        # no argument -> roll
        if value is None:
            return self.get_random()
        # too small argument -> 1
        if value < self.MIN_ROLL_VALUE:
            return self.MIN_ROLL_VALUE
        # too big argument -> 6
        if value > self.MAX_ROLL_VALUE:
            return self.MAX_ROLL_VALUE
        # ok argument
        return value

    def get_random(self) -> int:
        """ Get a random int value between 1 and 6 """
        return random.randint(self.MIN_ROLL_VALUE, self.MAX_ROLL_VALUE)

    def roll(self) -> None:
        """ Return a random value """
        #print("Rolled")
        self._value = self.get_random()

    def __str__(self) -> str:
        """ Value of a die as string """
        return str(self._value)

    def __eq__(self, arg) -> bool:
        """ Overwrite == operator """
        if isinstance(arg, Die):
            return self.value == arg.value
        if isinstance(arg, int):
            return self.value == arg
        return False
