#!/usr/bin/env python3
"""
Listen this module contains a coroutine to measure runtime
parallel async comprehension
"""
import asyncio
import time
async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """
    measure the time its takes to excute async_comprehension
    for time in parallel

    Return:
        float: Total runtime in seconds
    """
    start_time = time.perf_counter()
    await asyncio.gather(*(async_comprehension() for _ in range(4)))
    end_time = time.perf_counter()
    return end_time - start_time
