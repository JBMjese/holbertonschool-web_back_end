#!/usr/bin/env python3
"""a function that returns another function that multiplies x by
    the passed variable"""


from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """Create a function that multiplies a number by a given multiplier"""
    def multiply(number: float) -> float:
        """a Callable function that returns a float"""
        return number * multiplier
    return multiply
