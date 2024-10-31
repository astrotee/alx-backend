#!/usr/bin/env python3
"Basic dictionary"
from base_caching import BaseCaching


class BasicCache(BaseCaching):
    "Basic dictionary cache"
    def __init__(self) -> None:
        "init base class"
        super().__init__()

    def put(self, key, item):
        "cache a key-value"
        if None not in (key, item):
            self.cache_data[key] = item

    def get(self, key):
        "get a cached value by key"
        if key is None or key not in self.cache_data.keys():
            return None
        return self.cache_data[key]
