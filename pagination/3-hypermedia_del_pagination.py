#!/usr/bin/env python3
"""
Deletion-resilient hypermedia pagination
"""

import csv
import math
from typing import List, Dict


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None
        self.__indexed_dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset"""
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]  # skip header

        return self.__dataset

    def indexed_dataset(self) -> Dict[int, List]:
        """Dataset indexed by sorting position, starting at 0"""
        if self.__indexed_dataset is None:
            dataset = self.dataset()
            self.__indexed_dataset = {i: dataset[i] for i in range(len(dataset))}
        return self.__indexed_dataset

    def get_hyper_index(self, index: int = 0, page_size: int = 10) -> Dict:
    indexed_data = self.indexed_dataset()
    assert isinstance(index, int), "Index must be an integer"
    assert index >= 0, "Index must be non-negative"

    max_index = max(indexed_data.keys())
    assert index <= max_index, "Index out of range"

    # Move index forward if the requested index was deleted
    while index not in indexed_data and index <= max_index:
        index += 1

    data = []
    i = index
    collected = 0

    # Collect page_size items starting from the valid index
    while collected < page_size and i <= max_index:
        if i in indexed_data:
            data.append(indexed_data[i])
            collected += 1
        i += 1

    # Find next_index for next page
    next_index = None
    while i <= max_index:
        if i in indexed_data:
            next_index = i
            break
        i += 1

    return {
        "index": index,
        "next_index": next_index,
        "page_size": len(data),
        "data": data
    }
