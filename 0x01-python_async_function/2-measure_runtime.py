#!/usr/bin/env python3
"""measure the total execution time of wait_n"""
import asyncio
import time


wait_n = __import__('1-concurrent_coroutines.py').wait_n


async def measure_time(n: int, max_delay: int) -> float:
    """measure the total execution time of wait_n

    Args:
        n: The number of times it spins
        max_delay: The maximum number of seconds to wait.

    Returns:
        total_time/n
    """
    start_time = time.perf_counter()
    asyncio.run(wait_n(n, max_delay))
    total_time = time.perf_counter() - start_time

    return total_time / n
