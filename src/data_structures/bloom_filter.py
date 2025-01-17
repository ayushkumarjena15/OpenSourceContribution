import math

class BloomFilter:
    def __init__(self, capacity: int, fp_rate: float = 0.01):
        self.size = int(-(capacity * math.log(fp_rate)) / (math.log(2) ** 2))
        self.hash_count = max(1, int((self.size / capacity) * math.log(2)))
        self.bits = bytearray((self.size + 7) // 8)

    def add(self, item: str):
        for seed in range(self.hash_count):
            idx = hash((item, seed)) % self.size
            self.bits[idx // 8] |= (1 << (idx % 8))

    def contains(self, item: str) -> bool:
        for seed in range(self.hash_count):
            idx = hash((item, seed)) % self.size
            if not (self.bits[idx // 8] & (1 << (idx % 8))): return False
        return True
