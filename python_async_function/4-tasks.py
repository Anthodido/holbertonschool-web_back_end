#!/usr/bin/env python3
"""Module for task_wait_n function."""
import asyncio
from typing import List

task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """Spawn task_wait_random n times and return sorted delays."""
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
