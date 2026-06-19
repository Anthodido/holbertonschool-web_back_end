#!/usr/bin/env python3
"""Module for task_wait_random function"""

import asyncio

wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int) -> asyncio.Task:
    """Return an asyncio.Task for wait_random coroutine.

    Args:
        max_delay: maximum delay in seconds

    Returns:
        asyncio.Task wrapping wait_random
    """
    return asyncio.get_event_loop().create_task(wait_random(max_delay))
