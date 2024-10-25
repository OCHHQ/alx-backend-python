#!/usr/bin/env python3
"""
This module contains a function that measures the execution time of
wait_n and returns the average time per coroutine.
"""


import time
import asyncio
wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    """
    Measures the total execution time for wait_n(n, max_delay) and returns
    the average time per coroutine.

    Args:
        n (int): The number of times to spawn wait_random.
        max_delay (int): The maximum delay in seconds for each wait_random.

    Returns:
        float: The average execution time per coroutine.
    """
    start_time = time.time()  # Record the start time
    asyncio.run(wait_n(n, max_delay))  # Run the wait_n coroutine
    end_time = time.time()  # Record the end time

    total_time = end_time - start_time  # Calculate total elapsed time
    return total_time / n
