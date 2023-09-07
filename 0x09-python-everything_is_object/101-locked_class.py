#!/usr/bin/python3
"""
prevents the user from dynamically creating new instance attributes,
except if the new instance attribute is called first_name"""


from typing import Any


class LockedClass:
    __slots__ = ["first_name"]

    def __getattr__(self, name):
        if name != "firstname":
            raise AttributeError(f"'LockedClass' object \
                                has no attribute '{name}'")
