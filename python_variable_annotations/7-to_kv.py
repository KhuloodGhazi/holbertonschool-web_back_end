#!/usr/bin/env python3
"""Module to return a tuple of string and square of a number."""

from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """Return tuple (k, square of v as float)."""
    return (k, float(v ** 2))
