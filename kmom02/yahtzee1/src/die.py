""" Module for a die in yahtzee """
#!/usr/bin/env python3
import random
class Die():
    """ Die class """
    MIN_ROLL_VALUE = 1
    MAX_ROLL_VALUE = 6
    def __init__(self, _value = None):
        """ Die constructor """
        self._value = self.check_value(_value)

    def get_name(self):
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

    def get_value(self):
        """ Gets the value of a die """
        return self._value

    def check_value(self, value):
        """ Sets the value of a die based on input value """
        # no argument -> roll
        if value is None:
            return self.roll(True)
        # too small argument -> 1
        if value < self.MIN_ROLL_VALUE:
            return self.MIN_ROLL_VALUE
        # too big argument -> 6
        if value > self.MAX_ROLL_VALUE:
            return self.MAX_ROLL_VALUE
        # ok argument
        return value

    def roll(self, set_ret = None):
        """ Set a random value """
        #print("Rolled")
        rand_val = random.randint(self.MIN_ROLL_VALUE, self.MAX_ROLL_VALUE)
        if not set_ret:
            self._value = rand_val
        return rand_val

    def __str__(self):
        """ Value of a die as string """
        return str(self._value)
