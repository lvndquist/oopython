#!/usr/bin/env python3
""" Module implementing an unordered list """
from src.node import Node
from src.errors import MissingIndex, MissingValue

class UnorderedList():
    """Class representation of an unordered list"""
    def __init__(self, head = None) -> None:
        self._head = head

    @property
    def head(self):
        """Getter for head property"""
        return self._head

    @head.setter
    def head(self, head) -> None:
        """ Setter head property """
        self._head = head

    def append(self, data) -> None:
        """ Append node with data at end of list"""
        new_node = Node(data)

        # empty list
        if self.head is None:
            self.head = new_node
        else:
            current_node = self.head
            while current_node.next is not None:
                current_node = current_node.next
            current_node.next = new_node

    def set(self, index: int, data):
        """ Set the data of a node at index"""
        # empty list
        if self.head is None:
            raise MissingIndex("List is empty")

        current_node = self.head
        counter = 0

        # go to index
        while current_node is not None and counter < index:
            current_node = current_node.next
            counter =+ 1
        # replace data
        if counter == index:
            current_node.data = data
        # index not found
        else:
            raise MissingIndex("Invalid index")

    def size(self) -> int:
        """ Get the size of the list"""
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
        """Get the value at an index"""
        if self.head is None:
            raise MissingIndex("List is empty")
        if self.size() - 1 < index:
            raise MissingIndex("Index too big")
        if index < 0:
            raise MissingIndex("Index too small")
        current_node = self.head
        counter = 0
        while current_node is not None and counter < index:
            current_node = current_node.next
            counter += 1
        if counter == index:
            return current_node.data

    def index_of(self, value):
        """ Find index of a value, first occurance."""
        if self.head is None:
            raise MissingValue("List is empty")
        current_node = self.head
        index = 0
        while current_node is not None and current_node.data != value:
            current_node = current_node.next
            index += 1

        if current_node is None:
            raise MissingValue(f"{value} not found")
        return index

    def print_list(self):
        """ Print list """
        current_node = self.head
        ul_data = ""
        while current_node is not None:
            ul_data += str(current_node.data) + ", "
            current_node = current_node.next
        print(ul_data[:len(ul_data) - 2])
        #return ul_data

    def remove(self, data):
        """Remove a node with first occurance of data"""
        current_node = self.head
        previous_node = None

        if current_node is None:
            raise MissingValue("Empty list")

        while current_node is not None and current_node.data != data:
            previous_node = current_node
            current_node = current_node.next

        # value not found since its the end of the list
        if current_node is None:
            raise MissingValue(f"{data} not found")

        # previous never changed so the head is being removed
        if previous_node is None:
            self.head = current_node.next
            return current_node.data
        # value to remove found
        if current_node.data == data:
            previous_node.next = current_node.next
            return current_node.data

    def __len__(self) -> int:
        """ Overwrite len() for orderedlist class"""
        return self.size()

    def __str__(self) -> str:
        """ Overwrite str() for orderedlist class"""
        current_node = self.head
        ul_data = ""
        while current_node is not None:
            ul_data += str(current_node.data) + ", "
            current_node = current_node.next
        return ul_data[:len(ul_data) - 2]

    def __getitem__(self, key: int):
        """ Overwrite getitem() for orderedlist class """
        return self.get(key)

    def __setitem__(self, key: int, value):
        """ Overwrite setitem() for orderedlist class """
        return self.set(key, value)

if __name__ == "__main__":
    ul = UnorderedList()
    ul.append(1)
    ul.append(2)
    ul.append(3)
    print(len(ul))
    print(ul)
    print(ul[0])
    ul[0] = 22
    print(ul[0])
