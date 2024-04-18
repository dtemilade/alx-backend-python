#!/usr/bin/env python3
""" type-annotated function for duck type an iterable object
"""

from typing import Iterable, List, Sequence, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """ takes function’s parameters and return values with the appropriate types
    """
    return [(i, len(i)) for i in lst]
