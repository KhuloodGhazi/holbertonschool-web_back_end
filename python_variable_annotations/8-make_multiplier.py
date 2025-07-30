#!/usr/bin/env python3
"""Module that returns multiplier functions."""

from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """Return a function that multiplies input by multiplier."""

    def multiplier_func(n: float) -> float:
        return n * multiplier

    return multiplier_func
