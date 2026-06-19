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
    tasks = []
    for i in range(n):
        tasks.append(task_wait_random(max_delay))
 
    results = []
    for future in asyncio.as_completed(tasks):
        results.append(await future)
    return results
