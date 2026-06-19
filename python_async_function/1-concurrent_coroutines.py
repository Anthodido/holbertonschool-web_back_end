#!/usr/bin/env python3
"""Module for running multiple coroutines concurrently."""
import asyncio

wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int = 10) -> list[float]:
    """Spawn wait_random n times and return delays in ascending order.
 
    Args:
        n (int): Number of times to spawn wait_random.
        max_delay (int): Maximum delay in seconds.
 
    Returns:
        list: All delays in ascending order (via concurrency, not sort).
    """

    task = []
    for _ in range(n):
        task.append(asyncio.ensure_future(wait_random(max_delay)))

    results = []
    for result in asyncio.as_completed(task):
        results.append(await result)
    return results
