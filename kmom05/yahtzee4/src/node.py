#!/usr/bin/env python3
""" Class representing a node """

class Node():
    def __init__(self, data, next_ = None):
        """ Initialize single node """
        self.data = data
        self.next = next_
