#!/usr/bin/env python3
"""
This module contains an asynchronous routine that spawns multiple
coroutines concurrently and returns their results in ascending order.
"""


import asyncio
from typing import List
wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """
    Asynchronous routine that spawns wait_random n times with a maximum delay
    of max_delay seconds. It returns a list of delays in ascending order.
    Args:
        n (int): The number of times to spawn wait_random.
        max_delay (int): The maximum delay in seconds for each wait_random.
    Returns:
        List[float]: List of delays in ascending order.
    """
    # Create a list of tasks that call wait_random n times
    tasks = [asyncio.create_task(wait_random(max_delay)) for _ in range(n)]
    delays = [await task for task in asyncio.as_completed(tasks)]
    return sorted(delays)
