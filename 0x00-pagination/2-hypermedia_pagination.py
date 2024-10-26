#!/usr/bin/env python3
"pagination"


from typing import Dict, Tuple
import csv
import math
from typing import List


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    "get the index range for a page"
    start_index = page_size * (page - 1)
    end_index = start_index + page_size

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
            self.__dataset = dataset[1:]

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        "get a page"
        dataset = self.dataset()
        assert (type(page) is int and type(page_size) is int)
        assert (page > 0 and page_size > 0)
        start, end = index_range(page, page_size)
        if start > len(dataset) or end >= len(dataset):
            return []
        return dataset[start:end]

    def get_hyper(self, page: int = 1, page_size: int = 10) -> Dict:
        "Hypermedia pagination"
        data = self.get_page(page, page_size)
        _, end = index_range(page, page_size)
        total_size = len(self.dataset())
        return {
            'page_size': len(data),
            'page': page,
            'data': data,
            'next_page': page + 1 if end < total_size else None,
            'prev_page': page - 1 if page > 1 else None,
            'total_pages': math.ceil(total_size/page_size)
        }
