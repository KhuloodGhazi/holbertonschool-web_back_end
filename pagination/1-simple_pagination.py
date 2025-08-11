#!/usr/bin/env python3
"""
Simple pagination
"""

import csv
from typing import List, Tuple


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """
    Returns a tuple containing the start index and end index for a given page and page size.

    Args:
        page (int): The page number (1-indexed).
        page_size (int): The number of items per page.

    Returns:
        Tuple[int, int]: (start_index, end_index)
    """
    start_index = (page - 1) * page_size
    end_index = page * page_size
    return (start_index, end_index)


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]  # Skip header row

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """
        Returns a specific page of the dataset.

        Args:
            page (int): Page number (1-indexed), must be > 0.
            page_size (int): Number of items per page, must be > 0.

        Returns:
            List[List]: A list of rows for the given page.
        """
        # Validate arguments
        assert isinstance(page, int) and page > 0
        assert isinstance(page_size, int) and page_size > 0

        # Get start and end indexes
        start_index, end_index = index_range(page, page_size)

        dataset = self.dataset()

        # Return the slice, or empty list if start index is beyond dataset size
        if start_index >= len(dataset):
            return []

        return dataset[start_index:end_index]
