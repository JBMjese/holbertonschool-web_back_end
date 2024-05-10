#!/usr/bin/env python3
"""a coroutine called async_generator
that takes no arguments. """


import asyncio
import random
from typing import List, Generator


async def async_generator():
    """The coroutine Yields 10 random numbers between 0 and 10,
    with a 1-second delay between each yield."""
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.randint(0, 10)
