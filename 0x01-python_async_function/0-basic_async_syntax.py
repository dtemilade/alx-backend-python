#!/usr/bin/env python3
""" Asynchronous coroutine """

import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    """asyncronous function that return a float number
        with a random wait delay
    """

    random_val = random.uniform(0, max_delay)
    await asyncio.sleep(random_val)
    return random_val
