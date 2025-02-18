#!/usr/bin/env python3
""" Module implementing an a leaderboard """
from src.errors import MissingIndex, MissingValue
from src.unorderedlist import UnorderedList

class Leaderboard:
    """ Class representing a leaderboard, implemented using a unordered list"""
    def __init__(self, entries = None) -> None:
        if entries is not None:
            ul = UnorderedList()
            # entry like [(name, score), (..., ...)]
            for entry in entries:
                ul.append(entry)
            self.entries = ul
        else:
            self.entries = entries

    @classmethod
    def load(cls, filename: str) -> object:
        """ Load a file, returns a leaderboard object """
        try:
            with open(filename, 'r', encoding="utf-8") as file:
                loaded_entries = []
                for line in file:
                    entry = line.strip().split(", ")
                    loaded_entries.append((entry[0], entry[1], entry[2]))
                return cls(entries = loaded_entries)
        except FileNotFoundError:
            print(f"The file {filename} does not exist.")
            return None

    def save(self, filename: str) -> None:
        """ Save a file """
        if self.entries:
            try:
                with open(filename, 'w', encoding="utf-8") as file:
                    for index in range(self.entries.size()):
                        try:
                            entry = self.entries.get(index)
                            if entry is not None:
                                file.write(f"{entry[0]}, {entry[1]}, {entry[2]}\n")
                        except MissingIndex as e:
                            print(f"{e}")
            except IOError as e:
                print(f"Failed opening {filename}:\n{e}")

    def add_entry(self, name: str, score: int, date: str) -> None:
        """ Add an entry to the leaderboard """
        if self.entries:
            self.entries.append((name, score, date))

    def remove_entry(self, name: str, score: int, date: str) -> None:
        """ Remove an entry from the leaderboard"""
        if self.entries:
            try:
                self.entries.remove((name, score, date))
            except MissingValue as e:
                print(f"{e}")
