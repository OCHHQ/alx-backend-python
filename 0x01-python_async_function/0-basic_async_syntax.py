#!/usr/bin/env python3

import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    """
    Asynchronous coroutine that wait for a random
    deley btw 0 and max_delay sec.
    Args
        max_delay (int): the maximum delay in sec (default: 10).
    Return:
        float: the actual delay waited.
    """
    random_delay = random.uniform(0, max_delay)
    await asyncio.sleep(random_delay)
    return random_delay
