#!/usr/bin/env python3
"""Class representation of an unordered list"""
#from src.node import Node
from errors import MissingIndex
from node import Node

class UnorderedList():
    def __init__(self, head = None):
        self._head = head
    @property
    def head(self):
        return self._head
    
    @head.setter 
    def head(self, head):
        self._head = head

    def append(self, data):
        new_node = Node(data)

        # empty list
        if self.head is None:
            self.head = new_node
        else:
            current_node = self.head
            while current_node.next is not None:
                current_node = current_node.next
            current_node.next = new_node

    def set(self, index, data):
        # empty list
        if self.head is None:
            raise MissingIndex("List is empty")

        current_node = self.head
        counter = 0

        # go to index
        while current_node.next is not None and counter < index:
            current_node = current_node.next
            counter =+ 1
        # replace data
        if counter == index:
            current_node.data = data
        # index not found
        else:
            raise MissingIndex("Invalid index")
        pass

    def size(self):
        # empty list
        if self.head is None:
            return 0

        current_node = self.head
        counter = 0
        
        # go until last node
        while current_node is not None:
            current_node = current_node.next
            counter += 1
        # end of list 
        return counter

    def get(self, index):

        if self.head is None: 
            raise MissingIndex("List is empty")
        elif self.size() - 1 < index:
            raise MissingIndex("Index too big")
        elif index < 0:
            raise MissingIndex("Index too small")
        else:
            current_node = self.head
            counter = 0
            while current_node is not None and counter < index:
                current_node = current_node.next
                counter += 1
            if counter == index:
                return current_node.data

    def index_of(self, value):
        pass

    def print_list(self):
        pass

    def remove(self, data):
        pass
