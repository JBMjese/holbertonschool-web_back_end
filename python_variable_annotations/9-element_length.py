#!/usr/bin/env python3
"""Returns a list of tuples, where each tuple contains
an element of the list and its length"""


from typing import Sequence, List, Tuple, Iterable


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """return a sequence and int inside a tuple that inside a list"""
    return [(i, len(i)) for i in lst]
