#!/usr/bin/env python3
""" File for user defined exeptions """

class Error(Exception):
    """User defined class for custom exceptions"""

class MissingIndex(Error):
    """Index missing error"""

class MissingValue(Error):
    """Value missing error"""
