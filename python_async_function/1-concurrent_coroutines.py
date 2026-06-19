#!/usr/bin/env python3
"""Module for running multiple coroutines concurrently."""
import asyncio
from typing import List

wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """Spawn wait_random n times and return delays in ascending order."""
    delays: List[float] = []

    async def collect(delay: float) -> None:
        result = await wait_random(delay)
        for i, d in enumerate(delays):
            if result < d:
                delays.insert(i, result)
                return
        delays.append(result)

    await asyncio.gather(*[collect(max_delay) for _ in range(n)])
    return delays
