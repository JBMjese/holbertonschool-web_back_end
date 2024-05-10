#!/usr/bin/env python3
"""The coroutine will loop 10 times, each
time asynchronously wait 1 second, then
yield a random number between 0 and 10"""


import asyncio
import random
from typing import List, Generator


async def async_generator():
    for j in range(10):
        await asyncio.sleep(1)
        yield random.randint(0, 10)
