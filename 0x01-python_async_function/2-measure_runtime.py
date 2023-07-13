#!/usr/bin/env python3
"""Measure the runtime of coroutines"""
import asyncio
import time

wait_n = __import__('1-concurrent_coroutines').wait_n


async def measure_time(n: int, max_delay: int) -> float:
    """measure the total execution time of wait_n

    Args:
        n: The number of times it spins
        max_delay: The maximum number of seconds to wait.

    Returns:
        total_time/n
    """
    start_time: float = time.perf_counter()
    await wait_n(n, max_delay)
    end_time: float = time.perf_counter()
    total_time: float = end_time - start_time
    return (total_time/n)
