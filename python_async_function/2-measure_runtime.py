#!/usr/bin/env python3

import asyncio
import time
wait_n = __import__('1-concurrent_coroutines').wait_n

def measure_time(n: int, max_delay: int = 10) -> float:
    """Measure the total execution time for wait_n(n, max_delay).

    Args:
        n (int): The number of times to call wait_random.
        max_delay (int): The maximum number of seconds to wait.

    Returns:
        float: The total execution time in seconds.
    """
    start_time = time.time()
    asyncio.run(wait_n(n, max_delay))
    end_time = time.time()
    return (end_time - start_time) / n
