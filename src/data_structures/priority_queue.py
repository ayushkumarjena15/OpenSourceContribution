import heapq
from typing import Any

class PriorityQueue:
    def __init__(self):
        self._heap = []
        self._seq = 0

    def push(self, item: Any, priority: float):
        heapq.heappush(self._heap, (priority, self._seq, item))
        self._seq += 1

    def pop(self) -> Any:
        return heapq.heappop(self._heap)[2]

    def __len__(self): return len(self._heap)
