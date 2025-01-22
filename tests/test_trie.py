from src.data_structures.trie import Trie

def test_trie():
    t = Trie()
    t.insert('apple')
    assert t.search('apple') is True
    assert t.search('app') is False
    assert t.starts_with('app') is True
