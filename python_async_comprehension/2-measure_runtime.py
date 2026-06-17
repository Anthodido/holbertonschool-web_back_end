#!/usr/bin/env python3
"""Module for measuring runtime of parallel coroutines."""
import asyncio
import time

async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """Measures total runtime of 4 parallel async_comprehension calls."""
    start_time = time.time()
    await asyncio.gather(*(async_comprehension() for v in range(4)))
    end_time = time.time()
    total_time = end_time - start_time
    return total_time
#!/usr/bin/env python3
"""Module for measuring runtime of parallel coroutines."""
import asyncio
import time
async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """Measures total runtime of 4 parallel async_comprehension calls."""
    start_time = time.time()
    await asyncio.gather(*(async_comprehension() for v in range(4)))
    end_time = time.time()
    total_time = end_time - start_time
    return total_time
