#!/usr/bin/env python3
""" type-annotated function for Duck typing - first element of a sequence
"""

from typing import Any, Sequence, Union


def safe_first_element(lst: Sequence[Any]) -> Union[Any, None]:
    """ To duck-type elements of unknown inputs
    """
    if lst:
        return lst[0]
    else:
        return None
