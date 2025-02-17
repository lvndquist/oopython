#!/usr/bin/env python3
""" Module for a hand in yahtzee """
from die import Die

class Hand():
    """ Hand class """
    def __init__(self, dice_values = None) -> None:
        """ Constructor for hand """
        self.dice = self.set_values(dice_values)

    def roll(self, indexes = None) -> None:
        """ Rolls dice at specified indexes """
        # roll specified dice
        if indexes is not None:
            for index in indexes:
                self.dice[index] = Die()
        # roll all dice again
        else:
            for die in self.dice:
                die = die.roll()

    def set_values(self, dice_values) -> list[Die]:
        """ Sets values of the dice """
        dice_list = []

        # check if theres too many values
        if dice_values is not None and len(dice_values) > 5:
            dice_values = dice_values[:5]

        # no argument given
        if dice_values is None:
            for _ in range(5):
                dice_list.append(Die())

        # there is an argument and it has 5 values
        elif dice_values is not None and len(dice_values) == 5:
            for value in dice_values:
                dice_list.append(Die(value))

        # there is an argument but not with 5 values
        elif dice_values is not None and len(dice_values) < 5:
            # values from dice_values
            for value in dice_values:
                dice_list.append(Die(value))
            # fill out missing values
            missing_len = 5 - len(dice_values)
            for _ in range(missing_len):
                dice_list.append(Die())

        return dice_list

    def __str__(self) -> str:
        """ String representation of a hand """
        dice_str = ""
        for die in self.dice:
            dice_str += str(die) + ", "
        dice_str = dice_str[0:len(dice_str) - 2]
        return dice_str

    def to_list(self) -> list[int]:
        """ Convert a hand of dice to a list with dice values """
        dice_as_list = []
        for die in self.dice:
            dice_as_list.append(die.value)
        return dice_as_list

    def occurances(self) -> dict[int, int]:
        """ Count occurances in a hand using a dictionary """
        occurances = {}
        sorted_values = sorted(self.to_list())
        for value in sorted_values:
            if value in occurances:
                occurances[value] += 1
            else:
                occurances[value] = 1
        return occurances

    def sum(self) -> int:
        """ Get the sum of all dice in the hand """
        total = 0
        for value in self.to_list():
            total += value
        return total

    def has_sequence_of_length(self, length):
        """ Check if a hand has a consecutive sequence of some length like: 
            [1, 2, 3, 4, x]
            [2, 3, 4, 5, x]
            [3, 4, 5, 6, x]
            [1, 2, 3, 4, 5]
            [2, 3, 4, 5, 6]
        """
        occurances = list(set(self.occurances()))
        counter = 1
        for index, value in enumerate(occurances):
            # step past
            if index == 0:
                pass
            # previous value + 1 should be new value
            elif occurances[index - 1] + 1 == value:
                counter += 1
                if counter == length:
                    return True
            else:
                counter = 1
        return False
