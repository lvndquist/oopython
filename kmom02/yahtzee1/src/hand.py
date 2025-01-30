""" Module for a hand in yahtzee """
#!/usr/bin/env python3
from src.die import Die

class Hand():
    """ Hand class """
    def __init__(self, dice_values = None):
        """ Constructor for hand """
        self.dice = self.set_values(dice_values)

    def roll(self, indexes = None):
        """ Rolls dice at specified indexes """
        # roll specified dice
        if indexes is not None:
            for index in indexes:
                self.dice[index] = Die()
        # roll all dice again
        else:
            for die in self.dice:
                die = die.roll()

    def set_values(self, dice_values):
        """ Sets values of the dice """
        dice_list = []
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

    def __str__(self):
        """ String representation of a hand """
        dice_str = ""
        for die in self.dice:
            dice_str += str(die) + ", "
        dice_str = dice_str[0:len(dice_str) - 2]
        return dice_str
