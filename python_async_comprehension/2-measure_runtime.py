#!/usr/bin/env python3
"""Measure execution time of 4 async comprehensions running in parallel."""

import asyncio
import time
from typing import List
async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """Execute 4 async comprehensions in parallel and return total runtime."""
    start_time = time.time()
    await asyncio.gather(*(async_comprehension() for _ in range(4)))
    end_time = time.time()
    return end_time - start_time
