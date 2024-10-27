#!/usr/bin/env python3
"""
Deletion-resilient hypermedia pagination
"""

import csv
from typing import List, Dict, Optional


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None
        self.__indexed_dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def indexed_dataset(self) -> Dict[int, List]:
        """Dataset indexed by sorting position, starting at 0
        """
        if self.__indexed_dataset is None:
            dataset = self.dataset()
            # truncated_dataset = dataset[:1000]
            self.__indexed_dataset = {
                i: dataset[i] for i in range(len(dataset))
            }
        return self.__indexed_dataset

    def get_hyper_index(self, index: Optional[int] = None,
                        page_size: int = 10) -> Dict:
        "get page starting with index"
        idataset = self.indexed_dataset()
        keys = list(idataset.keys())
        assert (type(index) is int and index <= max(keys))
        start = index if index else 0
        count = 0
        page = []
        next_index = None
        for i in keys:
            if i >= start and count < page_size:
                page.append(idataset[i])
                count += 1
            elif count == page_size:
                next_index = i
                break
        return {
            'index': index,
            'next_index': next_index,
            'page_size': page_size,
            'data': page
        }
