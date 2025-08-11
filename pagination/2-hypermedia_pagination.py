import math
from typing import List, Dict, Any

class Server:
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset"""
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                import csv
                reader = csv.reader(f)
                next(reader)  # skip header
                self.__dataset = [row for row in reader]
        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """Return page of the dataset"""
        assert type(page) == int and page > 0
        assert type(page_size) == int and page_size > 0

        start_index = (page - 1) * page_size
        end_index = start_index + page_size
        dataset = self.dataset()
        return dataset[start_index:end_index]

    def get_hyper(self, page: int = 1, page_size: int = 10) -> Dict[str, Any]:
        """Return dictionary with pagination info and page data"""
        data = self.get_page(page, page_size)
        dataset_length = len(self.dataset())
        total_pages = math.ceil(dataset_length / page_size)

        hypermedia = {
            "page_size": len(data),
            "page": page,
            "data": data,
            "next_page": page + 1 if page < total_pages else None,
            "prev_page": page - 1 if page > 1 else None,
            "total_pages": total_pages
        }

        return hypermedia
