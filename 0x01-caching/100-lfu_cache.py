#!/usr/bin/env python3
"LFU caching"
from base_caching import BaseCaching


class LFUCache(BaseCaching):
    "Basic LFU cache"
    def __init__(self) -> None:
        "init base class"
        super().__init__()
        self.q = []
        self.counter = {}

    def put(self, key, item):
        "cache a key-value"
        if None not in (key, item):
            if key not in self.q and len(self.q) == self.MAX_ITEMS:
                k = self.lfu()
                self.q.remove(k)
                del self.counter[k]
                print(f"DISCARD: {k}")
                del self.cache_data[k]
            self.cache_data[key] = item
            if key not in self.q:
                self.q.append(key)
            if key not in self.counter.keys():
                self.counter[key] = 0

    def get(self, key):
        "get a cached value by key"
        if key is None or key not in self.cache_data.keys():
            return None
        self.q.remove(key)
        self.q.append(key)
        self.counter[key] = self.counter.get(key, 0) + 1
        return self.cache_data[key]

    def lfu(self):
        "get the key of the less frequently accessed item"
        lrfui = self.MAX_ITEMS
        min_value = min(self.counter.values())
        freq_keys = [key for key in self.counter.keys()
                     if self.counter[key] == min_value]
        if len(freq_keys) == 1:
            return freq_keys[0]
        for key in freq_keys:
            if lrfui > self.q.index(key):
                lrfui = self.q.index(key)
        return self.q[lrfui]
