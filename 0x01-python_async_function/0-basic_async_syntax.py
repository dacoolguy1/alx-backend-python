#!/usr/bin/env python3
import random
import asyncio
"""Write an asynchronous coroutine that takes in an integer argument"""


async def wait_random(max_delay=10):
    """
    Asynchronous coroutine that takes in an integer argument (max_delay)

    Args:
        max_delay(int): integer max no of secs to wait

    Return:
        The no of seconds waited
    """
    delay = random.uniform(0, max_delay)
    await asyncio.sleep(delay)
    # max_delay = 10
    return delay
