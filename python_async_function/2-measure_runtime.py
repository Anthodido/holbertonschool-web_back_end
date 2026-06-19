"""
Module qui mesure le temps d'exécution moyen de wait_n.
"""
import time
import asyncio
wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    """
    Mesure le temps total d'exécution de wait_n(n, max_delay)
    et retourne le temps moyen par coroutine (total_time / n).

    Args:
        n (int): nombre d'appels à wait_random.
        max_delay (int): délai maximum pour wait_random.

    Returns:
        float: temps moyen d'exécution.
    """
    start_time = time.time()
    asyncio.run(wait_n(n, max_delay))
    end_time = time.time()

    total_time = end_time - start_time
    return total_time / n
