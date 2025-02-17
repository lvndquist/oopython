#!/usr/bin/env python3
""" Node used in a list data structure """

class Node():
    """ Class representing a node """
    def __init__(self, data, next_ = None):
        """ Initialize single node """
        self.data = data
        self.next = next_
