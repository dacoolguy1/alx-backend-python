#!/usr/bin/env python3
"""Write an async args that takes in two argument"""
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
    """ # gather with an unpacked list of awaitables
    res = await asyncio.gather(*(wait_random(max_delay) for _ in range(n)))

    # Sort result in ascending order
    for i in range(len(res)):
        for j in range(i+1, len(res)):
            if (res[i] > res[j]):
                res[i], res[j] = res[j], res[i]

    return res
