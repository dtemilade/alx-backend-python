#!/usr/bin/env python3
""" Regular function
"""

import asyncio

wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int) -> asyncio.Task:
    """ Function that take the integer on max delay and return the task
    """
    return asyncio.create_task(wait_random(max_delay))
