#!/usr/bin/env python3
"""Async generator that yields numbers."""
import random
import asyncio


async def async_generator() -> int:
    """Async generator that yields numbers."""
    for i in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
