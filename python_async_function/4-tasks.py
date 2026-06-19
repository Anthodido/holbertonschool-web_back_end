#!/usr/bin/env python3
"""Module for task_wait_n using asyncio Tasks."""
import asyncio

task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int = 10) -> list:
        """Spawn task_wait_random n times and return delays in ascending order.
 
    Args:
        n (int): Number of tasks to spawn.
        max_delay (int): Maximum delay in seconds.
 
    Returns:
        list: All delays in ascending order.
    """
    delays = await asyncio.gather(
        *[task_wait_random(max_delay) for _ in range(n)])
    sorted_delays = []
    for delay in delays:
        inserted = False
        for i, val in enumerate(sorted_delays):
            if delay < val:
                sorted_delays.insert(i, delay)
                inserted = True
                break
        if not inserted:
            sorted_delays.append(delay)
    return sorted_delays
