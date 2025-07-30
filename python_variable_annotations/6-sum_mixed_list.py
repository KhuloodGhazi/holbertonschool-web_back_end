#!/usr/bin/env python3
"""Module to sum a mixed list of ints and floats."""

from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """Return the sum of a mixed list of ints and floats as a float."""
    return sum(mxd_lst)
