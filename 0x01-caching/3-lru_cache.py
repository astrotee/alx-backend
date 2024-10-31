#!/usr/bin/env python3
"LRU caching"
from base_caching import BaseCaching


class LRUCache(BaseCaching):
    "Basic LRU cache"
    def __init__(self) -> None:
        "init base class"
        super().__init__()
        self.q = []

    def put(self, key, item):
        "cache a key-value"
        if None not in (key, item):
            if key not in self.q and len(self.q) == self.MAX_ITEMS:
                k = self.q.pop(0)
                print(f"DISCARD: {k}")
                del self.cache_data[k]
            self.cache_data[key] = item
            if key not in self.q:
                self.q.append(key)

    def get(self, key):
        "get a cached value by key"
        if key is None or key not in self.cache_data.keys():
            return None
        self.q.remove(key)
        self.q.append(key)
        return self.cache_data[key]
