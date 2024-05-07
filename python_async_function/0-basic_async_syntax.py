#!/usr/bin/env python3
""" an asynchronous coroutine that takes in an integer argument"""


import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    """Generate a random delay between 0 and max_delay
    seconds and wait asynchronously"""
    delay = random.uniform(0, max_delay)
    await asyncio.sleep(delay)
    return delay
