#!/usr/bin/env python3
"""Write an async args that takes in two argument"""
from test import wait_random
import asyncio
from typing import List


wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """Asynchronous coroutine that waits for a random number
        of seconds between n and max_delay.

    Args:
        n: The number of times it spins
        max_delay: The maximum number of seconds to wait.

    Returns:
        The list of all delay.
    """
    delays: List[float] = []
    for _ in range(n):
        delay: float = await wait_random(max_delay)
        delays.append(delay)
    # delays.sort
    return sorted(delays)
