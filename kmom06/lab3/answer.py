#!/usr/bin/env python3

"""
44cd42d2c5ae1dcba3e1550b0d6a4b70
oopython
lab3
v2
jolq24
2025-02-19 15:15:57
v4.0.0 (2019-03-05)

Generated 2025-02-19 16:15:57 by dbwebb lab-utility v4.0.0 (2019-03-05).
https://github.com/dbwebb-se/lab
"""

from dbwebb import Dbwebb


# pylint: disable=invalid-name

dbwebb = Dbwebb()
dbwebb.ready_to_begin()



# ==========================================================================
# Lab 3 - Recursion
#
# If you need to peek at examples or just want to know more, take a look at
# the page: https://docs.python.org/3/library/index.html. Here you will find
# everything this lab will go through and much more.
#



# --------------------------------------------------------------------------
# Section 1. Simple recursion
#
# Practice on creating recursive functions.
#



# """"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
# Exercise 1.1 (1 points)
#
# Create a recursive function in the code below that calculates the sum of
# the numbers `12` up to `33`.
#
# Answer with the sum.
#
# Write your code below and put the answer into the variable ANSWER.
#

def recursive_sum(start, end):
    """ Sum from start to end"""
    if start <= end:
        return start
    sum_ = start + recursive_sum(start - 1, 12)
    return sum_
ANSWER = recursive_sum(33, 12)

# I will now test your answer - change false to true to get a hint.
dbwebb.assert_equal("1.1", ANSWER, False)

# """"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
# Exercise 1.2 (1 points)
#
# Create a recursive function in the code below that searches for the maximum
# element of a list and returns that number.
# Find the maximum value in the list `[2, 5, 1, 23, 11, 13, 21, 4, 6]`.
#
# Answer with the maximumx value.
#
# Write your code below and put the answer into the variable ANSWER.
#

def find_max(arr, length):
    """ Find maximum value in array"""
    if length == 1:
        return arr[0]

    rest = find_max(arr, length - 1)
    if rest < arr[length - 1]:
        return arr[length - 1]
    return rest

arr2 = [2, 5, 1, 23, 11, 13, 21, 4, 6]
ANSWER = find_max(arr2, len(arr2))

# I will now test your answer - change false to true to get a hint.
dbwebb.assert_equal("1.2", ANSWER, False)

# """"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
# Exercise 1.3 (1 points)
#
# Create a recursive function in the code below that searches a list for a
# number and returns the index of the number.
# Find the index of `6` in the list `[2, 5, 1, 23, 11, 13, 21, 4, 6]`.
# If the number cant be found, return -1.
#
# Answer with the index.
#
# Write your code below and put the answer into the variable ANSWER.
#

def find_index(arr, value, index = 0):
    """ Find index of value if it exists"""
    # terminate if index is bigger than list length
    if len(arr) <= index:
        return -1
    # index found
    if arr[index] == value:
        return index
    # go to next index
    return find_index(arr, value, index + 1)

arr3 = [2, 5, 1, 23, 1, 13, 21, 4, 6]

ANSWER = find_index(arr3, 6)


# I will now test your answer - change false to true to get a hint.
dbwebb.assert_equal("1.3", ANSWER, False)

# """"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
# Exercise 1.4 (1 points)
#
# Use the function from the previous assignment to find the number `10` in
# the list `[2, 5, 1, 23, 11, 13, 21, 4, 6]`.
#
# Answer with the index.
#
# Write your code below and put the answer into the variable ANSWER.
#

arr4 = [2, 5, 1, 23, 11, 13, 21, 4, 6]
ANSWER = find_index(arr4, 10)

# I will now test your answer - change false to true to get a hint.
dbwebb.assert_equal("1.4", ANSWER, False)

# """"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
# Exercise 1.5 (1 points)
#
# Create a recursive function in the code below that calculates `6` to the
# power of `6`.
#
# Answer with the result.
#
# Write your code below and put the answer into the variable ANSWER.
#

def recursive_power(base, exponent):
    """
    recursivly calculate base^exponent
    6^6 = 6 * 6^5 = 6 * 6 * 6^4 = ... = 6 * ... * 6
    """
    if exponent == 0:
        return 1
    return base * recursive_power(base, exponent - 1)

ANSWER = recursive_power(6, 6)

# I will now test your answer - change false to true to get a hint.
dbwebb.assert_equal("1.5", ANSWER, False)

# """"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
# Exercise 1.6 (1 points)
#
# Create a recursive function in the code below that turns a string
# backwards. Turn the string "Frontwards" backwards.
#
# Answer with the backward string.
#
# Write your code below and put the answer into the variable ANSWER.
#

def recursive_reverse(string):
    """Reverse string recursivly:
        F + rontwards
        r + ontwards
        o + ntwards
        n + twards
        t + wards
        w + ards
        a + rds
        r + ds
        d + s
        s
    """
    if len(string) <= 1:
        return string
    first = string[0]
    rest = string[1:]
    return recursive_reverse(rest) + first

ANSWER = recursive_reverse("Frontwards")

# I will now test your answer - change false to true to get a hint.
dbwebb.assert_equal("1.6", ANSWER, False)

# """"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
# Exercise 1.7 (1 points)
#
# Create a recursive function in the code below that calculates the "lowest
# common multiple" between two numbers.
# It should return the smallest positive integer that is divisible by both
# "6" and "6".
#
# Answer with the result.
#
# Write your code below and put the answer into the variable ANSWER.
#


def recursive_lcm(num1, num2, divider = 1):
    """ Recursively find the least common multiple."""
    # starting at 1 count up and check if both values are divisible by divider
    if divider % num1 == 0 and divider % num2 == 0:
        return divider
    # increase divider and go again
    return recursive_lcm(num1, num2, divider + 1)


ANSWER = recursive_lcm(6, 6)

# I will now test your answer - change false to true to get a hint.
dbwebb.assert_equal("1.7", ANSWER, False)


dbwebb.exit_with_summary()
