#!/usr/bin/env python3

import asyncio
wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int = 10) -> list:
    task = []
    for i in range(n):
        task.append(wait_random(max_delay))
    
    results = []
    for result in asyncio.as_completed(task):
        results.append(await result)
    return results
