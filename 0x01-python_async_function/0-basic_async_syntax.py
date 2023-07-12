#!/usr/bin/env python3
"""Write an asynchronous coroutine that takes in an integer argument"""
import random
import asyncio


async def wait_random(max_delay: int = 10) -> float:
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
