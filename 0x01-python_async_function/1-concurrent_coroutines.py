#!/usr/bin/env python3
from test import wait_random
import asyncio

"""Write an async args that takes in two argument"""


async def wait_n(n, max_delay):
   """
  Asynchronous coroutine that waits for a random number of seconds between n and max_delay.

  Args:
    n: The number of times it spins
    max_delay: The maximum number of seconds to wait.

  Returns:
    The list of all delay.
  """
#    wait_random = __import__('test.py').wait_random
   delays = []
   for _ in range(n):
      delay = await wait_random(max_delay)
      delays.append(delay)
   delays.sort
   return delays
