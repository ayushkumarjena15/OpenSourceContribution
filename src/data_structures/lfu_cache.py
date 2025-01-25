from collections import defaultdict, OrderedDict

class LFUCache:
    def __init__(self, capacity: int):
        self.cap = capacity
        self.min_freq = 0
        self.vals = {}
        self.freqs = {}
        self.lists = defaultdict(OrderedDict)

    def get(self, key: int) -> int:
        if key not in self.vals: return -1
        self._update(key)
        return self.vals[key]

    def put(self, key: int, value: int) -> None:
        if self.cap <= 0: return
        if key in self.vals:
            self.vals[key] = value
            self._update(key)
            return
        if len(self.vals) >= self.cap:
            k, _ = self.lists[self.min_freq].popitem(last=False)
            del self.vals[k]; del self.freqs[k]
        self.vals[key] = value
        self.freqs[key] = 1
        self.min_freq = 1
        self.lists[1][key] = None

    def _update(self, key: int):
        freq = self.freqs[key]
        self.freqs[key] += 1
        del self.lists[freq][key]
        if not self.lists[freq] and self.min_freq == freq:
            self.min_freq += 1
        self.lists[freq + 1][key] = None
