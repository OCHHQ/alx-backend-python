#!/usr/bin/env python3
"""
This module contains an asynchronous func that collect 10
random floats from async generator and return them in a list.
"""

from typing import List
async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    """
    collect 10 random floats from async generator
    """
    return [i async for i in async_generator()]
