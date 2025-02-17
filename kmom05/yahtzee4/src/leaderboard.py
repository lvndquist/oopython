#!/usr/bin/env python3
""" Module implementing an a leaderboard """
from errors import MissingIndex, MissingValue
from unorderedlist import UnorderedList

class Leaderboard:

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
        try:
            with open(filename, 'r') as file:
                loaded_entries = [] 
                for line in file:
                    entry = line.strip().split(", ")
                    loaded_entries.append((entry[0], entry[1]))
                return cls(entries = loaded_entries)
        except FileNotFoundError:
            print(f"The file {filename} does not exist.")
            return None

    def save(self, filename: str) -> None:
        if self.entries:
            try:
                with open(filename, 'w') as file:
                    for index in range(self.entries.size()):
                        try:
                            entry = self.entries.get(index)
                            if entry is not None:
                                file.write(f"{entry[0]}, {entry[1]}\n")
                        except MissingIndex as e:
                            print(f"{e}")
            except Exception as e:
                print(f"{e}")

    def add_entry(self, name: str, score: int) -> None:
        if self.entries:
            self.entries.append((name, score))

    def remove_entry(self, name: str, score: int) -> None:
        if self.entries:
            try:
                self.entries.remove((name, score))
            except MissingValue as e:
                print(f"{e}")
