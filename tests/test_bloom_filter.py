from src.data_structures.bloom_filter import BloomFilter

def test_bloom():
    bf = BloomFilter(100, 0.01)
    bf.add('hello')
    assert bf.contains('hello') is True
    assert bf.contains('world') is False
