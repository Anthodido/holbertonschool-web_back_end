#!/usr/bin/env python3

import asyncio
task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int = 10) -> list:
    task = []
    for i in range(n):
        task.append(task_wait_random(max_delay))
    
    results = []
    for result in asyncio.as_completed(task):
        results.append(await result)
    return results
