#!/usr/bin/env python3
""" type-annotated function forfloor
"""


def floor(n: float) -> int:
    """ takes float n as argument and returns the floor of the float as int.
    """
    return int(n) if n >= 0 else int(n) - 1
