from src.data_structures.lru_cache import LRUCache

def test_lru_cache():
    c = LRUCache(2)
    c.put('a', 1); c.put('b', 2)
    assert c.get('a') == 1
    c.put('c', 3) # evicts 'b'
    assert c.get('b') is None
    assert c.get('c') == 3
