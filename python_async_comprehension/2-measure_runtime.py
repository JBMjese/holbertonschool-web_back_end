#!/usr/bin/env python3
"""Measure the total runtime of running
async_comprehension four times in parallel."""

import time
from typing import List, Generator
import asyncio
async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """Run async_comprehension four
    times in parallel using asyncio.gather"""
    start = time.time()
    await asyncio.gather(async_comprehension())
    end = time.time()
    total = end - start
    return total
