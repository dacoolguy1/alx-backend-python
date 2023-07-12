#!/usr/bin/env python3
import random
import asyncio
"""Write an asynchronous coroutine that takes in an integer argument"""


async def wait_random(max_delay=10):
    """
    Asynchronous coroutine that takes in an integer argument (max_delay)

    Args:
        max_delay(int): integer

    Return:
        (int): random integer in the range
    """
    delay = random.randint(0, max_delay)
    await asyncio.sleep(delay)
    # max_delay = 10
    return delay

