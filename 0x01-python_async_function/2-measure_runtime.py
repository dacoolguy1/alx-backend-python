#!/usr/bin/env python3
"""measure the total execution time of wait_n"""
import asyncio
import time


wait_n = __import__('1-concurrent_coroutines.py').wait_n


def measure_time(n: int, max_delay: int) -> float:
    """measures the total execution time for wait_n(n, max_delay)

    Args:
        n (int): number of time wait _random should be callled.
        max_delay (int): delay period

    Returns:
        float: total execution time / n
    """
    start_time = time.perf_counter()
    asyncio.run(wait_n(n, max_delay))
    total_time = time.perf_counter() - start_time

    return total_time / n
