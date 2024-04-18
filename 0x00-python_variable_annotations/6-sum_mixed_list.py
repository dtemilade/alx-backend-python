#!/usr/bin/env python3
""" type-annotated function for sum_mixed_list
"""

from typing import List, Union


def sum_mixed_list(mxd_list: List[Union[int, float]]) -> float:
    """ takes a list mxd_lst of integers and floats and
        returns their sum as a float.
    """
    return sum(mxd_list)
