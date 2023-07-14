#!/usr/bin/env python3
""" A couroutine that loops 10 times"""
import asyncio
import time
import random
from typing import List


async def async_generator():
    """A coroutine that loops 10 times asynchronously

    Args:
        none

    return:
        random no
    """
    val: List = []
    for i in range(10):
        await asyncio.sleep(1)
        value = random.randint(0, 10)
        # val.append[value]
        yield value
