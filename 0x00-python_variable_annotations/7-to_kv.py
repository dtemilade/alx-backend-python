#!/usr/bin/env python3
""" type-annotated function for TO_KV
"""

from typing import List, Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """ takes a string k & an int OR float v as arguments and returns a tuple
    """
    return (k, v**2)
