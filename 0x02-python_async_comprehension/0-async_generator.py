#!/usr/bin/env python3
""" coroutine called async_generator that takes no arguments.
"""

import random
import asyncio
from typing import Generator


async def async_generator() -> Generator[float, None, None]:
    """ The coroutine will loop 10 times, each time asynchronously
        random number between 0 and 10. Use the random module.
    """
    for i in range(10):
        await asyncio.sleep(1)
        yield random.random() * 10
