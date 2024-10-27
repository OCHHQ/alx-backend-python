#!/usr/bin/env python3
"""
This module contains an asynchronous generator function that yields
a random float between 0 and 10 after waiting 1 second, 10 times in total.
"""

import asyncio
import random
from typing import AsyncGenerator


async def async_generator() -> AsyncGenerator[float, None]:
    """
    Yields a random float between 0 and 10 every second, 10 times in total.
    """
    for _ in range(10):
        await asyncio.sleep(1)  # Wait 1 second asynchronously
        yield random.uniform(0, 10)  # Yield a random float between 0 and 10
