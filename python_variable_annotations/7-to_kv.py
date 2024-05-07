#!/usr/bin/env python3
"""converts a key-value pair into a tuple with the key as a string
and the value squared as a float."""


from typing import List, Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """pass the first element as str and multiply the others"""
    return (k, v * v)
