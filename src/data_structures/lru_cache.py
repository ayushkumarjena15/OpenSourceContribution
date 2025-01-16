import threading
from typing import Any, Optional, Dict

class Node:
    def __init__(self, key: Any, val: Any):
        self.key, self.val = key, val
        self.prev = self.next = None

class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.map = {}
        self.head, self.tail = Node(None, None), Node(None, None)
        self.head.next, self.tail.prev = self.tail, self.head
        self._lock = threading.Lock()

    def get(self, key: Any) -> Any:
        with self._lock:
            if key not in self.map: return None
            node = self.map[key]
            self._remove(node); self._insert(node)
            return node.val

    def put(self, key: Any, val: Any) -> None:
        with self._lock:
            if key in self.map: self._remove(self.map[key])
            elif len(self.map) >= self.capacity:
                lru = self.tail.prev
                self._remove(lru); del self.map[lru.key]
            n = Node(key, val); self._insert(n); self.map[key] = n

    def _remove(self, node: Node) -> None:
        node.prev.next, node.next.prev = node.next, node.prev

    def _insert(self, node: Node) -> None:
        node.next, node.prev = self.head.next, self.head
        self.head.next.prev, self.head.next = node, node
